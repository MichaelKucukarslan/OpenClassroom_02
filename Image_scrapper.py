import os
import requests # request img from web
import shutil # save img locally

file_name = "foldername/save.img"
class Image_Scrapper:
    def image_scrapper(self, image_url, category, book_title):
        res = requests.get(image_url, stream = True)
        if res.status_code == 200:
            try:
                os.makedirs('./book_covers/' + category, exist_ok=True)
                with open('./book_covers/' + category + '/' + book_title + '.jpg','wb') as f:
                    shutil.copyfileobj(res.raw, f)
            except OSError:
                pass
        else:
            print('Image Couldn\'t be retrieved')

url = "http://books.toscrape.com/media/cache/fe/72/fe72f0532301ec28892ae79a629a293c.jpg"
take = Image_Scrapper()
take.image_scrapper(url, "category", "title of book")