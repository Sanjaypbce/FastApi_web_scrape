import requests
from bs4 import BeautifulSoup

def scrape(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        soup = BeautifulSoup(response.content, 'html.parser')

        # Example: Scrape all headings (h1, h2, h3, h4, h5, h6)
        headings = []
        for i in range(1, 7):
            for heading in soup.find_all(f'h{i}'):
                headings.append(heading.get_text(strip=True))

        return {"headings": headings}
    except requests.RequestException as e:
        return {"error": str(e)}
