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

# This is code that will get one page of books from one category
first_category = url + book_categories[0]
page_two = requests.get(first_category)
soup_2 = BeautifulSoup(page_two.text, "html.parser")
big_book_list = []
# .product_pod h3 a "These are where the links are"
for link in soup_2.select('.product_pod h3 a'):
    text_link = link.get('href')
    text_link = url + "catalogue" + text_link[8:]
    big_book_list.append(text_link)

for item in big_book_list:
    print(item)

print("good job")
# Figure out Paganation
# Do milestone 3
# TODO: turn code into functions
# TODO: get the category saved to go into the csv file
# TODO: get information from those books
# TODO: get the next page if available
    # use a counter to count to the next page
    # there is a pager class for categories with more than one page
# TODO: Get images of the books
