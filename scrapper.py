from bs4 import BeautifulSoup
from os import system

# set page url and grap html file
url = "https://boards.4channel.org/w/thread/2174128"
system("curl " + url + " >> index.html")

# parse and extract jpg and png files
with open("index.html", 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, "lxml")

    links = []
    for link in soup.find_all("a"):
        links.append(link.get('href'))

    pics_jpg = [x for x in links if "jpg" in x]
    pics_png = [x for x in links if "png" in x]

    print("getting ready to download png files...")
    for pic_png in pics_png:
        system("wget https:" + pic_png)
        print(pic_png + " is downloaded.")

    print("getting ready to download jpg files...")
    for pic_jpg in pics_jpg:
        system("wget https:" + pic_jpg)
        print(pic_jpg + " is downloaded.")

    system("rm *.jpg.1*")
    system("rm *.png.1*")
