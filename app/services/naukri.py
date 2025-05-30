import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

def search(query, location=None, experience=None, job_age=None):
    base_url = "https://www.naukri.com/"
    query_str = quote(query)
    location_str = f"&location={quote(location)}" if location else ""
    experience_str = f"&experience={experience}" if experience else ""
    job_age_str = f"&jobAge={job_age}" if job_age else ""
    url = f"{base_url}{query_str}-jobs?k={query_str}{location_str}{experience_str}{job_age_str}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        jobs = []
        for job_card in soup.find_all('article', class_='jobTuple'):
            title = job_card.find('a', class_='title')
            company = job_card.find('a', class_='subTitle')
            location_tag = job_card.find('li', class_='location')
            salary_tag = job_card.find('li', class_='salary')
            experience_tag = job_card.find('li', class_='experience')
            posted_tag = job_card.find('span', class_='job-post-time')
            
            jobs.append({
                'title': title.text.strip() if title else None,
                'company': company.text.strip() if company else None,
                'location': location_tag.text.strip() if location_tag else None,
                'salary': salary_tag.text.strip() if salary_tag else None,
                'experience': experience_tag.text.strip() if experience_tag else None,
                'posted_date': posted_tag.text.strip() if posted_tag else None,
                'url': title['href'] if title and title.has_attr('href') else None,
                'source': 'naukri'
            })
        return jobs
    except Exception as e:
        print(f"Error fetching Naukri jobs: {str(e)}")
        return [] 