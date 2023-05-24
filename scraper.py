import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'

# page = requests.get(URL)

def get_citations_needed_count(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    citations_needed = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    return len(citations_needed)

# print(get_citations_needed_count(URL)) #12

def get_citations_needed_report(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    citations_needed = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
    report = ""
    for citation in citations_needed:
        passage = citation.find_parent('p').text.strip()
        report += f"Citation needed for \"{passage}\"\n\n"
    return report

print(get_citations_needed_report(URL))