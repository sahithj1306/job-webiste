# Job Aggregator API

A FastAPI-based job search aggregator that combines job listings from multiple sources including Adzuna, Remotive, Naukri, and Foundit.

## Features

- Search jobs across multiple platforms simultaneously
- Filter by location and experience
- Deduplicated results
- RESTful API interface

## Setup

1. Clone the repository:
```bash
git clone https://github.com/sahithj1306/job-website.git
cd job-website
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### GET /search

Search for jobs across multiple platforms.

Query Parameters:
- `query` (required): Job title or keywords
- `location` (optional): Location to search in
- `experience` (optional): Years of experience required

Example:
```
GET /search?query=python&location=remote&experience=2
```

## Supported Job Platforms

- Adzuna
- Remotive
- Naukri
- Foundit

## Development

To add a new job platform:
1. Create a new service file in `app/services/`
2. Implement the search function
3. Add the service to the imports in `main.py`
4. Add the service to the search endpoint

## License

MIT 