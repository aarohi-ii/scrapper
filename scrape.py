git config --global user.name "Aarohi Parajuli"
git config --global user.email "aarohiparajuli7@gmail.com"


import json
import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"


def scrape_books(url):
    response = requests.get(url)
    
    if response.status_code != 200:
        return[]
    
    # Set encoding explicitly to handle special characters correctly
    response.encoding = response.apparent_encoding
    
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    
    all_books = []
    for book in books:
        title = book.h3.a['title']
        price_text = book.find("p", class_="price_color").text
        currency = price_text[0]
        price = float(price_text[1:])
        all_books.append(
            {
                "title": title,
                "price": price,
                "currency": currency,
            }
            )
        
    return all_books
        
books = scrape_books(url)

with open("books.json", "w", encoding='utf-8') as f:
   json.dump(books, f, indent=4, ensure_ascii=False)