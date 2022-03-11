from PIL import Image
import requests
from bs4 import BeautifulSoup
from io import BytesIO
import urllib.request as ur
import numpy as np

url = 'https://nhentai.net/tag/' + input('Input a tag: ')

r = requests.get(url)
if r.status_code != 200:
    exit('Result not found')
soup = BeautifulSoup(r.text, "html.parser")
rows = soup.findAll('div', class_='gallery')
for i in range(1,11):
    captions = rows[i].find('div').text
    print(i,'. ',captions)
index = int(input('Enter a number to get the cover page: '))
content = rows[index-1].find('img')
src = content.get('data-src')
print(src)
response = requests.get(src)
img = Image.open(BytesIO(response.content))
img.show()