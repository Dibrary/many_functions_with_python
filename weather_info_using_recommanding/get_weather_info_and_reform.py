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

pty_code = {"0":"없음","1":"비","2":"비/눈","3":"눈","4":"소나기","5":"빗방울","6":"빗방울/눈날림","7":"눈날림"}

data = dict()
data['date'] = base_date
weather = dict()

res = requests.get(vilage_weather_url)
try:
    items = res.json().get('response').get('body').get('items')
    for item in items['item']:
        if item['category'] == 'T3H':
            weather['tmp'] = item['fcstValue']
        if item['category'] == 'PTY':
            weather['code'] = item['fcstValue']
            weather['state'] = pty_code[item['fcstValue']]
except:
    print("날씨정보 가져오기 실패:", res.text)

data['weather'] = weather
print(data['weather'])


