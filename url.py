
from lxml import etree
import requests

def get_img(URL_login,headers):
    html = requests.get(URL_login,headers = headers)
    selector = etree.HTML(html.text)
    with open('/Users/huangrenming/Desktop/hhh.html','wb') as file:
        file.write(html.content)
    img = selector.xpath('//*[@id="randomPhoto"]/img/@src')
    

def main():
    headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Mobile Safari/537.36'}
    url = 'http://jwc.swjtu.edu.cn/vatuu/UserFramework'
    URL_login = 'http://jwc.swjtu.edu.cn/service/login.html'
    get_img(URL_login,headers)
    data ={
        'username': '2018111510',
        'password': 'asdasdasd',
        'url': 'http://jwc.swjtu.edu.cn/index.html',
        'ranstring': 'tojf',
        }
    
    # requests.post(URL_login,headers = headers,data = data)
    # html = requests.get(url,headers = headers)
    # print (html.text)

if __name__ == '__main__':
    main()
