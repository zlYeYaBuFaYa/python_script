from bs4 import BeautifulSoup
import requests

# soup = BeautifulSoup('<b class="boldest" id="b_id">Extremely bold</b>', 'html.parser')

# print(soup.prettify())

# print(soup.b)
# print(soup.b.name)
# print(soup.b.string)
# print(soup.b['class'])

# print(type(soup.b.string))
# print(soup.b.attrs)

# <a class="downButton" href="http://dzs.xqishuta.net/23/23842/万相之王.txt" title="《万相之王》全集打包下载">Txt格式下载</a>

url = "http://dzs.xqishuta.net/23/23842/万相之王.txt"

response = requests.get(url)


with open("./万相之王.txt", "wb") as f:
    f.write(response.content)
