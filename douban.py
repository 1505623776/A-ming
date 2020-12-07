import requests
import wordcloud
from lxml import etree
import time
import pandas
def main():
    num = input('电影编号:')
    text = ''
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Safari/605.1.15'}
    for i in range(10):
        time.sleep(2)
        page = i
        print('爬取第%s页'%page)
        url = 'https://movie.douban.com/subject/%s/comments?start=%s&limit=20&status=P&sort=new_score'%(num,(page*20))
        html = requests.get(url,headers = headers).text
        selector = etree.HTML(html)
        try:
            title = selector.xpath('//*[@id="content"]/h1/text()')[0]
        except:
            pass
        try:
            reviews = selector.xpath('//*[@id="comments"]/div')
        except:
            pass
        for rev in reviews:
            try:
                review = rev.xpath('.//*[@class=" comment-content"]/span/text()')[0]
                print(review)
                text+=review+'\n'
            except:
                pass
            
            
    with open ('/Users/huangrenming/Desktop/douban/%s.txt'%title,'wb') as file:
        file.write(text.encode("utf-8")) 
    w = wordcloud.WordCloud(scale=4,
    max_font_size=80,
    min_font_size=10,
    width=1000,
    height=700,
    background_color="white",
    font_path='/System/Library/AssetsV2/com_apple_MobileAsset_Font6/61c49f4632f9c10ad2521da713cda25f94f77be3.asset/AssetData/SimSong.ttc')
    w.generate(text)
    w.to_file('/Users/huangrenming/Desktop/douban/%s.png'%title)





if __name__ == "__main__":
    main()