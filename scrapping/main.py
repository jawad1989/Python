# https://scrapy.org/
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
import requests
from bs4 import BeautifulSoup
import pprint

# first page
res     = requests.get('https://news.ycombinator.com/')
soup    = BeautifulSoup(res.text,'html.parser')
links   = soup.select(".storylink")
subtext = soup.select('.subtext')

# second page
res2      = requests.get('https://news.ycombinator.com/news?p=2')
soup2     = BeautifulSoup(res.text,'html.parser')
links2    = soup2.select(".storylink")
subtext2  = soup2.select('.subtext')

mega_links   = links + links2
mega_subtext = subtext + subtext2


def sort_news_by_votes(hnlist):
    return sorted(hnlist, key = lambda hn:hn['points'],reverse=True)
   

def create_custom_hn(links,subtext):
    hn = []
    for idx, item in enumerate(links):
        title  = item.getText()
        href   = item.get('href', None)
        vote   = subtext[idx].select('.score')
    
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points  > 100:
                hn.append({'title': title, 'href': href, 'points': points})
    return sort_news_by_votes(hn)

res = create_custom_hn(mega_links,mega_subtext)
pprint.pprint(res)


# TESTING
# print(res)
# print(res.text)
# print(soup.prettify())
# print(soup.body.contents)
# print(soup.find_all('div'))
# print(soup.title)
# print(soup.a)
# print(soup.find(id="score_27259321"))


# CSS Selectors
# print(len(soup.select(".storylink")))
# print(soup.select(".storylink")[0])
# print(score[0].get("id"))
