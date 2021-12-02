import urllib.request, urllib.parse, urllib.error
import requests
from bs4 import BeautifulSoup
import ssl
import re
from datetime import datetime, timedelta

def status_check(r):
    if r.status_code == 200:
        # print("Success!")
        return 1
    else:
        # print("Failed!")
        return -1


def get_yesterday():
    yesterday = datetime.now() - timedelta(1)
    return datetime.strftime(yesterday, '%Y-%m-%d')


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Read the HTML from the URL and pass on to BeautifulSoup
top100url = 'https://www.gutenberg.org/browse/scores/top'
response = requests.get(top100url)
# print(response.content)

status_check(response)

contents = response.content.decode(response.encoding)

ebooks_tmp = contents.split('<h2 id="books-last1">Top 100 EBooks yesterday</h2>\n\n<ol>\n',1)[1]
ebooks = ebooks_tmp.split('\n</ol>\n <div class="padded">\n  <ul>\n')[0]
soup = BeautifulSoup(ebooks, 'html.parser')

ebooks_set = {}

for link in soup.find_all('a'):
    ebooks_set[link.get('href').split("/ebooks/")[-1]] = link.text

print(f"The top 100 ebooks from yesterday ({get_yesterday()}) on gutenberg.org site are below:\n")
for k in ebooks_set.keys():
    if int(k) > 999:
        print(f"BookNumber: {k}\tBookName: {ebooks_set[k]}")
    else:
        print(f"BookNumber: {k}\t\tBookName: {ebooks_set[k]}")

# Read the HTML from the URL and pass on to BeautifulSoup
top40url = "https://top40weekly.com/"
response = requests.get(top40url)

status_check(response)

contents = response.content.decode(response.encoding)

songs_tmp = contents.split('</div><hr class="x-line e447-9 mcf-3"></hr><div id="" class="x-text" style=""><p>',1)[1]
songs = songs_tmp.split('</div><div id="" class="x-text" style=""><p><iframe loading="lazy" src="about:blank" width="300" height="380" frameborder="0" allowtransparency="true"',1)[0]
soup = BeautifulSoup(songs, 'html.parser')

top40 = soup.text.splitlines()

print("\n\n\n\n")
print(f"The top 40 songs on top40weekly.com/ site are below:\n")
for i in top40:
    if i:
        print(i.strip())