import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

from app.api.routes import router as api_router

app = FastAPI(
    title="Graph Coloring Exam Timetabling & Seating Plan Generator",
    description="Automated examination scheduling and room-wise seating plan generator using Greedy & DSATUR graph coloring algorithms.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

# Mount static files if frontend build exists
frontend_dist = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "frontend", "dist")
if os.path.exists(frontend_dist):
    app.mount("/static", StaticFiles(directory=frontend_dist), name="static")

@app.get("/", response_class=HTMLResponse)
def root_index():
    """
    Renders an embedded, interactive web control dashboard for timetable generation,
    conflict graph visualization (Cytoscape.js), algorithm comparison, and seating plan exports.
    """
    html_dashboard_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "frontend", "index.html")
    if os.path.exists(html_dashboard_path):
        with open(html_dashboard_path, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())

    return HTMLResponse(content="""
    <!DOCTYPE html>
    <html>
      <head><title>Exam Timetable & Seating Generator API</title></head>
      <body style="font-family: sans-serif; padding: 2rem; background: #0f172a; color: #f8fafc;">
        <h1>Exam Timetabling & Seating Plan Generator API</h1>
        <p>Backend engine is running.</p>
        <p><a href="/docs" style="color: #38bdf8;">View Swagger API Documentation</a></p>
      </body>
    </html>
    """)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
