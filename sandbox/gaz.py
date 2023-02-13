from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

# Sample: https://diy.sndimg.com/content/dam/images/diy/fullset/2011/1/20/0/DIY_art-deco-home-exterior_s3x4.jpg.rend.hgtvcom.616.822.suffix/1420692209594.jpeg
url = "https://www.hgtv.com/design/decorating/design-101/popular-architectural-home-styles-pictures"

link = urlopen(url).read()
soup = BeautifulSoup(link, "html.parser")

imgList = soup.findAll("img")

for i in imgList:
    print()
    # print(type(i))
    attributes = i.attrs
    print(attributes)
    if i.has_attr("src"):
        imgUri = "src:" + i["src"]
    elif i.has_attr("data-src"):
        imgUri = "data-src: " + i["data-src"]
    else:
        imgUri = ""

    print(imgUri)
