import requests
from bs4 import BeautifulSoup

#  url here
url = 'https://portal.ucc.edu.gh'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

links = []
for link in soup.find_all('a'):
    href = link.get('href')
    if href is not None:
        links.append(href)

print(links)
