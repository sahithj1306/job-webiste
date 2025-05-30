from fastapi import FastAPI, Query
from typing import List, Optional
from app.services import adzuna, remotive, naukri, foundit
from app.merger import merge_jobs

app = FastAPI()

@app.get("/search")
async def search_jobs(
    query: str = Query(..., description="Job title or keywords"),
    location: Optional[str] = None,
    experience: Optional[int] = Query(None, description="Years of experience required"),
    job_age: Optional[int] = Query(None, description="Job posting age in days")
):
    jobs = []
    jobs += adzuna.search(query, location)
    jobs += remotive.search(query, location)
    jobs += naukri.search(query, location, experience, job_age)
    jobs += foundit.search(query, location)
    jobs = merge_jobs(jobs)
    return {"results": jobs} 