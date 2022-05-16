
import requests
import json
import datetime

vilage_weather_url = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst?"

service_key = "동네예보조회 인증키 입력"
base_date = datetime.datetime.today().strftime("%Y%m%d")
base_time = "0800"
nx = "59"
ny = "126"

payload = "serviceKey="+service_key+"&"+"dataType=json"+"&" \
                                                        "base_date="+base_date +"&" \
                                                                                "base_time="+base_time+"&" \
                                                                                                       "nx="+nx+"&" \
                                                                                                                "ny="+ny
res = requests.get(vilage_weather_url + payload)
try:
    items = res.json().get('response').get('body').get('items')
    print(items)
except:
    print("날씨정보 요청 실패", res.text)



