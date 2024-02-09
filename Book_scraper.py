import requests, csv
from bs4 import BeautifulSoup

URL = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
page = requests.get(URL)

soup = BeautifulSoup(page.text, 'html.parser')

# Most of the needed information is in the table towards the bottom. Find all the tds and place them in the appropriate section
coloumns = soup.find_all('td')
upc = coloumns[0].text.strip()
price_including_tax = coloumns[2].text.strip()
price_excluding_tax = coloumns[3].text.strip()
quantity_available = coloumns[5].text.strip()

# Other information was around the html page
product_page_url = URL
category_of_book = soup.find_all('a')[3].text
title = soup.find('h1').text 
product_description = soup.find_all('p')[3].text 
image_url = soup.find('img')['src']
rating = soup.find('p', class_="star-rating").get("class")[1]


with open('book_file.csv', mode='w') as books:
    books_writer = csv.writer(books, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    books_writer.writerow(["product_page_url", "category", "book title", "review_rating", "image_url", "product_description", 
                           "upc",  "price_including_tax", "price_excluding_tax", "quantity_available"])
    books_writer.writerow([product_page_url, category_of_book, title, rating, image_url, 
                           product_description, upc, price_including_tax, price_excluding_tax, quantity_available])
