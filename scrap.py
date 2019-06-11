import requests
import bs4
res = requests.get('https://google.com')
type(res)

res.text

soup = bs4.BeautifulSoup(res.text,'html')
ci = soup('title')
ci
ci[0].getText()

boup = bs4.BeautifulSoup(res.text,'lxml')
di = boup('head')
di
di[0].getText()

#all links
for link in soup.find_all('a'):
...     print(link.get('href'))