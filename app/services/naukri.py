import requests
from bs4 import BeautifulSoup

def search(query, location=None):
    base_url = "https://www.naukri.com/"
    query_str = query.replace(" ", "-")
    location_str = f"-jobs-in-{location.replace(' ', '-')}" if location else ""
    url = f"{base_url}{query_str}-jobs{location_str}?k={query_str}"
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
            jobs.append({
                'title': title.text.strip() if title else None,
                'company': company.text.strip() if company else None,
                'location': location_tag.text.strip() if location_tag else None,
                'salary': salary_tag.text.strip() if salary_tag else None,
                'url': title['href'] if title and title.has_attr('href') else None,
                'source': 'naukri'
            })
        return jobs
    except Exception as e:
        return [] 