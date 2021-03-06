
import requests
from bs4 import BeautifulSoup
import bs4.element
import datetime

def get_soup_obj(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.151 Whale/3.14.134.62 Safari/537.36'}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')

    return soup
default_img = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=naver#"
for sid in ['100']:#, '101', '102']:
    sec_url="https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1="+ sid
    print("section url : ", sec_url)

    soup = get_soup_obj(sec_url)

    lis3 = soup.find('ul', class_='type06_headline').find_all('li', limit=3)
    for li in lis3:
        news_info = {
            "title":li.img.attrs.get('alt') if li.img
                    else li.a.text.replace("\n", "")
                            .replace("\t","").replace("\r",""),
            "date":li.find(class_="date").text,
            "news_url":li.a.attrs.get('href'),
            "image_url":li.img.attrs.get('src') if li.img else default_img
        }
        print(news_info)
        # 정상으로 출력됨.

        



