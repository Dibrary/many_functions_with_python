
import requests
from bs4 import BeautifulSoup
import bs4.element
import datetime

def get_soup_obj(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.151 Whale/3.14.134.62 Safari/537.36'}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    return soup

def get_top3_news_info(sec, sid):
    default_img = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=naver#"

    sec_url="https://news.naver.com/main/list.nhn?mode=LSD&mid=sec&sid1="+ sid
    print("section url: ", sec_url)

    soup = get_soup_obj(sec_url)

    news_list3 = []
    lis3 = soup.find('ul', class_='type06_headline').find_all('li', limit=3)
    for li in lis3:
        news_info = {
            "title": li.img.attrs.get('alt') if li.img else li.a.text.replace('\n', "").replace('\t','').replace('\r', ''),
            "date": li.find(class_='date').text,
            "news_url":li.a.attrs.get('href'),
            "image_url":li.img.attrs.get('src') if li.img else default_img
        }
        news_list3.append(news_info)
    return news_list3

def get_news_contents(url):
    soup = get_soup_obj(url)
    # print(soup) # 여기서 출력은 되지만, article_body_contents라는 class를 가진 부분이 없어서 body가 None이 됨. 그래서 for문에서 에러 남.

    body = soup.find('div', class_='_article_body_contents')

    news_contents = ''
    for content in body:
        if type(content) is bs4.element.NavigableString and len(content) > 50:
            news_contents += content.strip() + ' '
    return news_contents

def get_naver_news_top3():
    news_dic = dict()
    sections = ['pol','eco','soc']
    section_ids = ['100', '101', '102']
    for sec,sid in zip(sections, section_ids):
        news_info = get_top3_news_info(sec, sid)
        for news in news_info:
            news_url= news['news_url']
            news_contents = get_news_contents(news_url)
            news['news_contents'] = news_contents
        news_dic[sec] = news_info
    return news_dic

news_dic = get_naver_news_top3()
news_dic['eco'][0]






