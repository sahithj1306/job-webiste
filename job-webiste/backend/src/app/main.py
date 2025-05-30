from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.services import adzuna, remotive, naukri, foundit
from app.merger import merge_jobs

app = FastAPI(title="Job Search API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to Job Search API"}

@app.get("/search")
async def search_jobs(
    query: str,
    location: str = None,
    experience: int = None
):
    jobs = []
    jobs += adzuna.search(query, location)
    jobs += remotive.search(query, location)
    jobs += naukri.search(query, location, experience)
    jobs += foundit.search(query, location)
    jobs = merge_jobs(jobs)
    return {"results": jobs} 