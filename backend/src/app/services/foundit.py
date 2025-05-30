import requests
from bs4 import BeautifulSoup

def search(query, location=None):
    base_url = "https://www.foundit.in"
    query_str = query.replace(" ", "-")
    url = f"{base_url}/srp/results?query={query_str}"
    if location:
        url += f"&locations={location.replace(' ', '%20')}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
    }
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, 'html.parser')
        jobs = []
        for job_card in soup.find_all('div', class_='card-apply-content'):  # class may change, update as needed
            title = job_card.find('h3')
            company = job_card.find('span', class_='company-name')
            location_tag = job_card.find('span', class_='loc')
            salary_tag = job_card.find('span', class_='package')
            link = job_card.find('a', href=True)
            jobs.append({
                'title': title.text.strip() if title else None,
                'company': company.text.strip() if company else None,
                'location': location_tag.text.strip() if location_tag else None,
                'salary': salary_tag.text.strip() if salary_tag else None,
                'url': base_url + link['href'] if link else None,
                'source': 'foundit'
            })
        return jobs
    except Exception as e:
        return [] 