
import random, requests
from get_microdust_info_and_reform import data

rain_foods = "부대찌개,아구찜,해물탕,칼국수,수제비,우동".split(",")

pmhigh_foods = "콩나물국밥,고등어,굴,쌀국수".split(",")

def get_foods_list(weather, dust_pm10, dust_pm20):
    if weather != "0":
        recommand_state = "Case1"
        foods_list = random.sample(rain_foods, k=len(rain_foods))
    elif dust_pm10 == "매우나쁨" or dust_pm20 == "매우나쁨":
        recommand_state = 'Case2'
        foods_list = random.sample(pmhigh_foods, k=len(pmhigh_foods))
    else:
        recommand_state = 'Case3'
        foods_list = ['']
    return recommand_state, foods_list

def naver_local_search(query, display):
    headers = {
        "X-Naver-Client-Id":"네이버 애플리케이션 Client ID",
        "X-Naver-Client-Secret":"네이버 애플리케이션의 Client Secret"
    }

    params = {
        "sort":"comment",
        "query":query,
        "display":display
    }

    naver_local_url = "https://openapi.naver.com/v1/search/local.json"

    res = requests.get(naver_local_url, headers=headers, params=params)
    places = res.json().get('items')

    return places

weather = data.get('weather').get('code')
dust_pm10 = data.get('dust').get('PM10').get('state')
dust_pm20 = data.get('dust').get('PM2.5').get('state')

weather_state, foods_list = get_foods_list(weather, dust_pm10, dust_pm20)

location = "문래동"

recommands = []
for food in foods_list:
    query = location+" "+food +"맛집"
    result_list = naver_local_search(query, 3)

    if len(result_list) > 0:
        if weather_state == "Case3":
            recommands = result_list
            break
        else:
            recommands.append(result_list[0])
    else:
        print("검색 결과 없음")

    if len(recommands) == 3:
        break

print(recommands)



