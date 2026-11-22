from fastapi import APIRouter, HTTPException
from app.models.schemas import (
    TimetableGenerationRequest,
    TimetableResponse,
    AlgorithmType,
    AlgorithmMetrics,
)
from app.services.timetable_generator import TimetableGeneratorService
from app.services.conflict_graph import ConflictGraphBuilder
from app.services.graph_coloring import GraphColoringService
from app.api.sample_data import get_default_sample_data

router = APIRouter(prefix="/api", tags=["Timetable & Graph Coloring"])

@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Graph Coloring Exam Timetabling & Seating Plan Generator",
        "version": "1.0.0"
    }

@router.get("/sample-data")
def get_sample_data():
    """Returns sample academic dataset containing students, courses, exams, and rooms."""
    return get_default_sample_data()

@router.post("/timetable/generate", response_model=TimetableResponse)
def generate_timetable(request: TimetableGenerationRequest):
    """
    Generates a conflict-free timetable using either Greedy Coloring or DSATUR,
    allocates rooms according to capacities, and produces room-wise seating plans.
    """
    try:
        if not request.exams:
            raise HTTPException(status_code=400, detail="At least one examination must be provided.")
        if not request.rooms:
            raise HTTPException(status_code=400, detail="At least one room must be provided.")

        response = TimetableGeneratorService.generate(request)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Generation failed: {str(e)}")

@router.post("/timetable/compare")
def compare_algorithms(request: TimetableGenerationRequest):
    """
    Runs both Greedy Coloring and DSATUR on the exact same conflict graph,
    returning detailed comparative performance metrics (slots used, runtime, distribution).
    """
    try:
        builder = ConflictGraphBuilder(request.exams, request.students)
        adjacency, shared_map = builder.build_graph()

        greedy_coloring, greedy_metrics = GraphColoringService.greedy_coloring(adjacency)
        dsatur_coloring, dsatur_metrics = GraphColoringService.dsatur_coloring(adjacency)

        # Graph stats
        total_nodes = len(request.exams)
        total_conflicts = len(shared_map)

        return {
            "total_examinations": total_nodes,
            "total_conflicts": total_conflicts,
            "greedy_metrics": greedy_metrics,
            "dsatur_metrics": dsatur_metrics,
            "slots_saved_by_dsatur": max(0, greedy_metrics.slots_used - dsatur_metrics.slots_used),
            "recommendation": "DSATUR achieves optimal or near-optimal time slot minimization by dynamically prioritizing vertices with highest color saturation."
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Comparison failed: {str(e)}")
