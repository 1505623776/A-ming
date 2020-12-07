from urllib import request
from urllib.parse import quote
import requests
import numpy
from lxml import etree
import pandas
import string
import time
import random
movies = []
for i in range(5):
    url_search = 'https://movie.douban.com/review/best/?start=%d' %(i*20)
    print(i)
    # url_search = quote(url_search, safe = string.printable)

    headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Mobile Safari/537.36'}
    req = requests.get(url_search,headers = headers)
    selector = etree.HTML(req.text)
    # webdata = request.urlopen(req).read()
    urls = selector.xpath('//*[@id="content"]/div/div[1]/div[1]/div')
    
    for url in urls:
        movie_url = (url.xpath('.//*[@class="subject-img"]/img/@title'))[0]
        name = (url.xpath('.//*[@class="name"]/text()'))[0]
        short_review = (url.xpath('.//*[@class="short-content"]/text()'))[0].replace(' ','').replace('\n','')
        if short_review == '':
            short_review = (url.xpath('.//*[@class="short-content"]/text()'))[1].replace(' ','').replace('\n','')
        movie = {'movie':movie_url,'name':name,'review':short_review}
        
        movies.append(movie)

moviedata = pandas.DataFrame(movies)
moviedata.to_csv('/Users/huangrenming/Desktop/movie.csv')


# with open('/Users/huangrenming/Desktop/htt.html','wb') as file:
#     file.write(req.content)

# req = request.Request(url = url_search,headers = headers)
# html_search = request.urlopen(req).read()
# time.sleep(5)
# selector = etree.HTML(reqe.txt)

# url = selector.xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]/div[1]/div/div[3]/text()')

# with open('/Users/huangrenming/Desktop/video/ht.html','wb') as file:
#     file.write()

