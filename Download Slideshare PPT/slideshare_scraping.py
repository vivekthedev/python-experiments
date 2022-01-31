import requests
from bs4 import BeautifulSoup
from PIL import Image
import io
URL_LESS = "https://www.slideshare.net/angelucmex/global-warming-2373190?qid=8f04572c-48df-4f53-b2b0-0eb71021931c&v=&b=&from_search=1"
URL="https://www.slideshare.net/tusharpanda88/python-basics-59573634?qid=03cb80ee-36f0-4241-a516-454ad64808a8&v=&b=&from_search=5"
r = requests.get(URL_LESS)

soup = BeautifulSoup(r.content, "html5lib")

imgs = soup.find_all('img', class_="slide-image")
imgSRC = [x.get("srcset").split(',')[-2].strip().split(' ')[0].split('?')[0] for x in imgs]


imagesJPG = []
for img in imgSRC:
    im = requests.get(img)
    f = io.BytesIO(im.content)
    imgJPG = Image.open(f)
    imagesJPG.append(imgJPG)

imagesJPG[0].save(f"{soup.title.string}.pdf",save_all=True, append_images=imagesJPG[1:])
