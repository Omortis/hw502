from gazpacho import get, Soup
import os

if os.name == "posix":
    os.system("clear")
else:
    os.system("cls")

# html = get(url)
# soup = Soup(html)
# books = soup.find('div', {'class': 'book-'}, partial=True)

# def parse(book):
#     name = book.find('h4').text
#     price = float(book.find('p').text[1:].split(' ')[0])
#     return name, price

# [parse(book) for book in books]

# Sample: https://diy.sndimg.com/content/dam/images/diy/fullset/2011/1/20/0/DIY_art-deco-home-exterior_s3x4.jpg.rend.hgtvcom.616.822.suffix/1420692209594.jpeg
url = "https://www.hgtv.com/design/decorating/design-101/popular-architectural-home-styles-pictures"

html = get(url)
soup = Soup(html)

imgList = soup.find("img")

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
