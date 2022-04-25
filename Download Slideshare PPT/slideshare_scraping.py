import requests
from bs4 import BeautifulSoup
from PIL import Image
import io
from termcolor import colored
from colorama import init
import sys
import tqdm
import os

init()

cover = "Free Slideshare"
c_cover = colored(cover, "green")
print(c_cover)
ask = colored("Paste your Link here ", "red")
print(ask)
link = input("")

if link:

    try:
        r = requests.get(link)
    except requests.exceptions.MissingSchema:
        msg = colored("please paste a valid link", "red")
        print(msg)
        print("Press any key to Exit")
        input("")

    else:
        soup = BeautifulSoup(r.content, "html5lib")
        title = str(soup.title.string)
        msg = colored("fetching link content...", "blue")
        print(msg)

        imgs = soup.find_all("img", class_="slide-image")
        if len(imgs) < 1:
            msg = colored(
                "looks like the powerpoint does not exists, please try a different link",
                "red",
            )
            print(msg)
            print("Press any key to Exit")

            input("")
            sys.exit(1)

        msg = colored("stripping slides link...", "green")
        print(msg)

        imgSRC = [
            x.get("srcset").split(",")[-2].strip().split(" ")[0].split("?")[0]
            for x in imgs
        ]
        msg = f"found {len(imgSRC)} slides "
        print(msg)
        imagesJPG = []
        for img in tqdm.tqdm(imgSRC):
            try:
                im = requests.get(img)
                f = io.BytesIO(im.content)
            except:
                msg = colored(
                    "looks like your network connection is the culprit here, connect to a better connection then try again.",
                    "red",
                )
                print(msg)
                print("Press any key to Exit")
                input("")
                sys.exit(1)
            else:
                imgJPG = Image.open(f)
                imagesJPG.append(imgJPG)

        title = title + ".pdf"
        imagesJPG[0].save(title, save_all=True, append_images=imagesJPG[1:])
        msg = f"file saved at {os.getcwd()}/{title}"
        msg = colored(msg, "green")
        print(msg)
        print("Press any key to Exit")
        input("")
