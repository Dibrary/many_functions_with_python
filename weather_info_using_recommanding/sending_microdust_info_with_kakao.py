
import json
from kakaoTALK_sending.taking_token import *
from get_microdust_info_and_reform import data

KAKAO_TOKEN_FILENAME = "res/kakao_token.json"
KAKAO_APP_KEY = "REST_API 앱 키 입력"
update_tokens(KAKAO_APP_KEY, KAKAO_TOKEN_FILENAME)

weather_url = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8"

text = f"""
기온: {data['weather']['tmp']}
기우: {data['weather']['state']}
미세먼지: {data['dust']['PM10']['value']} {data['dust']['PM10']['state']}
초미세먼지: {data['dust']['PM2.5']['value']} {data['dust']['PM2.5']['state']}
"""

template = {
    "object_type":"text",
    "text":text,
    "link":{
        "web_url":weather_url,
        "mobile_web_url":weather_url
    },
    "button_title":"날씨 상세보기"
}

res = send_message(KAKAO_TOKEN_FILENAME, template)
if res.json().get('result_code') == 0:
    print("성공적으로 보냄")
else:
    print("실패", res.json())


