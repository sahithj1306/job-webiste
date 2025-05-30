import requests

def search(query, location=None):
    url = "https://remotive.com/api/remote-jobs"
    params = {"search": query}
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        jobs = []
        for job in data.get("jobs", []):
            jobs.append({
                "title": job.get("title"),
                "company": job.get("company_name"),
                "location": job.get("candidate_required_location"),
                "salary": job.get("salary"),
                "url": job.get("url"),
                "source": "remotive"
            })
        return jobs
    except Exception as e:
        return [] 