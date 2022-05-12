
import requests

headers = {
    'X-Naver-Client-Id':'네이버 애플리케이션 Client ID',
    'X-Naver-Client-Secret':'네이버 애플리케이션의 Client Secret'
}

query='국민대 맛집'
params = {
    'sort':'comment',
    'query':query,
    'display':3
}

naver_local_url = 'https://openapi.naver.com/v1/search/local.json'

res = requests.get(naver_local_url, headers=headers, params=params)

if res.status_code == 200:
    places = res.json().get('items')
    print(places)

