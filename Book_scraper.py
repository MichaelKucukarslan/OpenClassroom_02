import requests
from bs4 import BeautifulSoup

class BookScraper:
# Create a function that scrapes the book's info
    def web_address_to_book_info_list(self, url_address):
        page = requests.get(url_address)
        soup = BeautifulSoup(page.text, 'html.parser')
        # Most of the needed information is in the table towards the bottom. Find all the tds and place them in the appropriate section
        columns = soup.find_all('td')
        upc = columns[0].text.strip()
        price_including_tax = columns[2].text.strip()
        price_excluding_tax = columns[3].text.strip()
        quantity_available = columns[5].text.strip()

        # Other information was around the html page
        product_page_url = url_address
        category_of_book = soup.find_all('a')[3].text
        title = soup.find('h1').text 
        product_description = soup.find_all('p')[3].text.strip()
        # added to get the correct image url
        url = "http://books.toscrape.com/"
        image_url = url + soup.find('img')['src'][6:]
        rating = soup.find('p', class_="star-rating").get("class")[1]
        return [product_page_url, category_of_book, title, rating, image_url, 
                            product_description, upc, price_including_tax, price_excluding_tax, quantity_available]    
