import requests
from bs4 import BeautifulSoup

base_url = "http://books.toscrape.com/catalogue/page-{}.html"
page = 1
titles = []

while True:
    url = base_url.format(page)

    response = requests.get(url)
    if response.status_code != 200:

    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.select("article.product_pod h3 a")

    if not books:
        break

    for book in books:
        title = book["title"]
        titles.append(title)

    page += 1

for i, t in enumerate(titles, start=1):
    print(f"{i}. {t}")

print(f"\nЗагалом знайдено: {len(titles)} книг.")
