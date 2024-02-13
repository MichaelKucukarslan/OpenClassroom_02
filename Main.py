# This main file will find all the main categories on the online bookstore
from bs4 import BeautifulSoup
import requests, csv, time
from Book_scraper import Book_scraper
from tqdm import tqdm

url = "http://books.toscrape.com/"
web_page = requests.get(url)

soup = BeautifulSoup(web_page.text, "html.parser")
categories = soup.find(class_="side_categories").find_all('a')

# get all categories from the main page
all_categories_from_main_page = []
print("Getting all Categories from main page: ")
for category in tqdm(categories):
    all_categories_from_main_page.append(url + category.get("href"))
# The first one is the sample page which doesn't need to be saved so pop it
all_categories_from_main_page.pop(0) 

big_book_list = []
# This is code that will get all pages of books from one category
def get_links_from_one_category(site_url):
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
        get_links_from_one_category(new_page)

# used to get the last '/' in the urls to get the next page on longer categories
def find_all_char_pos_in_string(string, character):
    return [i for i, ltr in enumerate(string) if ltr == character]

print("Getting all books from one category:")
for item in tqdm(all_categories_from_main_page):
    get_links_from_one_category(item)

# Scrape the book and put them into a CSV file without loading a list into memory
print("Getting all book's information:")
bs = Book_scraper()
with open('book_file.csv', mode='w') as books:
    books_writer = csv.writer(books, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    books_writer.writerow(["product_page_url", "category", "book title", "review_rating", "image_url", "product_description", 
                           "upc",  "price_including_tax", "price_excluding_tax", "quantity_available"])
    for item in tqdm(big_book_list):
        books_writer.writerow(bs.web_address_to_book_info_list(item))
