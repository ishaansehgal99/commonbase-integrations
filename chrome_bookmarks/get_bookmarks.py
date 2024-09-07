import json

from bs4 import BeautifulSoup

# load the bookmarks html file
with open('bookmarks.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

bookmarks = []

# find all the bookmark links
for link in soup.find_all('a'):
    title = link.get_text()
    url = link.get('href')
    bookmarks.append({'title': title, 'author': url})

# save to a json file
with open('bookmarks.json', 'w', encoding='utf-8') as file:
    json.dump(bookmarks, file, indent=4, ensure_ascii=False)

