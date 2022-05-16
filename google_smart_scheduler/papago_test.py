

import requests
client_id = 'X-Client-아이디'
client_secret = 'X-Client-비밀번호'

url = "https://openapi.naver.com/v1/papago/n2mt"
headers = {'X-Naver-Client-Id':client_id,
           'X-Naver-Client-Secret':client_secret}
data =  { 'source': 'ko',
         'target': 'en',
         'text': '안녕하세요'.encode('utf-8')} # utf-8로 한글 사용

res = requests.post(url, data=data, headers=headers) # POST 형식으로 API 사용
print(res.json()) # json 형식으로 res 열람