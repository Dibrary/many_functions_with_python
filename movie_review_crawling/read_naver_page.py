import requests
from bs4 import BeautifulSoup

url = "https://movie.naver.com/movie/bi/mi/review.nhn?code=191633"

res = requests.get(url)

soup = BeautifulSoup(res.text, "lxml")
ul = soup.find("ul", class_="rvw_list_area") # class가 같은 ul태그를 찾음
lis = ul.find_all("li") # ul을 기준으로 li태그를 찾는다.

count = 0
for li in lis:
    count += 1
    print(f"[{count}th] ", li.a.string)