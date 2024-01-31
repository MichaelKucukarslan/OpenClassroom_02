# This main file will find all the main categories on the online bookstore
from bs4 import BeautifulSoup
import requests

url = "http://books.toscrape.com/"
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

categories = soup.find(class_="side_categories").find_all('a')

cat2 = []
for item in categories:
    cat2.append(item.get("href"))
cat2.pop(0)
print(cat2)