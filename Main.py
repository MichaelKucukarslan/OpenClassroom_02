# This main file will find all the main categories on the online bookstore
from bs4 import BeautifulSoup
import requests

url = "http://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

categories = soup.find(class_="side_categories").find_all('a')

book_categories = []
for item in categories:
    book_categories.append(item.get("href"))
book_categories.pop(0)
# print(book_categories)

# This is code that will get one page of books from one category
first_category = url + book_categories[0]
page_two = requests.get(first_category)
soup_2 = BeautifulSoup(page_two.text, "html.parser")
big_book_list = []
# .product_pod h3 a
for link in soup_2.select('.product_pod h3 a'):
    text_link = link.get('href')
    text_link = url + "catalogue" + text_link[8:]
    big_book_list.append(text_link)

for item in big_book_list:
    print(item)


# Get the books from the page
# TODO: get the next page if available
    # there is a pager class for categories with more than one page
     
# http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html
