# This main file will find all the main categories on the online bookstore
from bs4 import BeautifulSoup
import requests
from Book_scraper import Book_scraper

url = "http://books.toscrape.com/"
web_page = requests.get(url)

soup = BeautifulSoup(web_page.text, "html.parser")
categories = soup.find(class_="side_categories").find_all('a')

# get all categories from the main page
# TODO: Remove category list if no longer needed
book_categories_web_address = []
book_categories_type = []
for book in categories:
    book_categories_web_address.append(book.get("href"))
    book_categories_type.append(book.text.strip())
# The first one is the sample page which doesn't need to be saved so pop it
book_categories_web_address.pop(0) 
book_categories_type.pop(0)

# This is code that will get all pages of books from one category
big_book_list = []
first_category = url + book_categories_web_address[0]
def get_links_for_one_category(site_url):
    page_two = requests.get(site_url)
    soup_2 = BeautifulSoup(page_two.text, "html.parser")
    # .product_pod h3 a "These are where the links are"
    for link in soup_2.select('.product_pod h3 a'):
        text_link = link.get('href')
        text_link = url + "catalogue" + text_link[8:]
        big_book_list.append(text_link)
    # Check for more books on next page
    next_page = soup_2.select('.pager .next a')
    if next_page:
        list_of_backspaces = find_all_char_pos_in_string(site_url, '/')
        new_page = site_url[:list_of_backspaces[-1]] + '/' + next_page[0].get('href')
        get_links_for_one_category(new_page)

def find_all_char_pos_in_string(string, character):
    return [i for i, ltr in enumerate(string) if ltr == character]

get_links_for_one_category(first_category)

# TODO: Create function that takes a url and get back a list to put into a csv file
all_books_info = []
bs = Book_scraper()
for book in big_book_list:
    all_books_info.append(bs.web_address_to_book_info_list(book))

for book in all_books_info:
    print(book)
# Do milestone 3
# TODO: get the category saved to go into the csv file
# TODO: get information from those books
# TODO: get the next page if available
    # use a counter to count to the next page
    # there is a pager class for categories with more than one page
# TODO: Get images of the books
