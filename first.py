import requests

URL = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
page = requests.get(URL)

print(page.text)