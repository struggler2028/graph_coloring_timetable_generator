import time
from typing import Dict, Set, List, Tuple
from collections import Counter
from app.models.schemas import AlgorithmMetrics

def validate_coloring(adjacency: Dict[str, Set[str]], coloring: Dict[str, int]) -> bool:
    """Verifies that no two adjacent vertices share the same color."""
    for u, neighbors in adjacency.items():
        if u not in coloring or coloring[u] is None:
            return False
        for v in neighbors:
            if v in coloring and coloring[u] == coloring[v]:
                return False
    return True

class GraphColoringService:
    @staticmethod
    def greedy_coloring(adjacency: Dict[str, Set[str]]) -> Tuple[Dict[str, int], AlgorithmMetrics]:
        """
        Greedy Graph Coloring Algorithm:
        - Iterates over vertices sequentially (ordered by exam id / initial sequence).
        - For each vertex, assigns the smallest available color not used by neighbors.
        """
        start_time = time.perf_counter()
        
        coloring: Dict[str, int] = {}
        # Deterministic vertex ordering
        vertices = sorted(list(adjacency.keys()))

        for u in vertices:
            # Gather colors currently assigned to neighbors
            neighbor_colors = {
                coloring[v] for v in adjacency.get(u, set())
                if v in coloring and coloring[v] is not None
            }

            # Find smallest non-negative color not used by any neighbor
            color = 0
            while color in neighbor_colors:
                color += 1
            
            coloring[u] = color

        elapsed_ms = (time.perf_counter() - start_time) * 1000.0
        
        slots_used = len(set(coloring.values())) if coloring else 0
        color_dist = dict(Counter(coloring.values()))
        is_valid = validate_coloring(adjacency, coloring)

        metrics = AlgorithmMetrics(
            algorithm_name="Greedy Coloring",
            slots_used=slots_used,
            execution_time_ms=round(elapsed_ms, 3),
            color_distribution=color_dist,
            is_valid_coloring=is_valid,
            unallocated_students_count=0
        )

        return coloring, metrics

    @staticmethod
    def dsatur_coloring(adjacency: Dict[str, Set[str]]) -> Tuple[Dict[str, int], AlgorithmMetrics]:
        """
        DSATUR (Degree of Saturation) Graph Coloring Algorithm:
        - Saturation degree = number of different colors assigned to adjacent neighbors.
        - Picks the uncolored vertex with highest saturation degree.
        - Tie-breaking rule: vertex with highest overall degree in the graph.
        - Dynamically assigns the lowest available color and updates neighbor saturation.
        """
        start_time = time.perf_counter()

        coloring: Dict[str, int] = {}
        uncolored: Set[str] = set(adjacency.keys())
        degrees = {u: len(adjacency.get(u, set())) for u in adjacency}

        # Cache of neighbor colors for fast saturation calculation
        neighbor_colors_map: Dict[str, Set[int]] = {u: set() for u in adjacency}

        while uncolored:
            # 1. Select uncolored vertex with highest saturation degree
            best_vertex = None
            max_sat = -1
            max_deg = -1

            for u in uncolored:
                sat = len(neighbor_colors_map[u])
                deg = degrees[u]

                if sat > max_sat:
                    max_sat = sat
                    max_deg = deg
                    best_vertex = u
                elif sat == max_sat:
                    # Tie-breaking by maximum degree
                    if deg > max_deg or (deg == max_deg and (best_vertex is None or u < best_vertex)):
                        max_deg = deg
                        best_vertex = u

            if best_vertex is None:
                break

            # 2. Assign the smallest available color
            used_colors = neighbor_colors_map[best_vertex]
            color = 0
            while color in used_colors:
                color += 1

            coloring[best_vertex] = color
            uncolored.remove(best_vertex)

            # 3. Update saturation degrees of all adjacent neighbors
            for nbr in adjacency.get(best_vertex, set()):
                neighbor_colors_map[nbr].add(color)

        elapsed_ms = (time.perf_counter() - start_time) * 1000.0

        slots_used = len(set(coloring.values())) if coloring else 0
        color_dist = dict(Counter(coloring.values()))
        is_valid = validate_coloring(adjacency, coloring)

        metrics = AlgorithmMetrics(
            algorithm_name="DSATUR",
            slots_used=slots_used,
            execution_time_ms=round(elapsed_ms, 3),
            color_distribution=color_dist,
            is_valid_coloring=is_valid,
            unallocated_students_count=0
        )

        return coloring, metrics
