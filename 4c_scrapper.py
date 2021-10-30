from bs4 import BeautifulSoup
from os import system
from bs4.element import ProcessingInstruction

# set page url here
url = "https://boards.4channel.org/w/thread/2207595"
system("curl " + url + " >> index.html")

with open("index.html", 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, "lxml")

    links = []
    for link in soup.find_all("a"):
        links.append(link.get('href'))

    pics = [x for x in links if "jpg" in x or "png" in x]
    pics = list(dict.fromkeys(pics))

    for pic in pics:
        system("wget https:" + pic)
