
from sending_microdust_info_with_kakao import weather_url
from weather_info_using_recommanding.dish_data_with_weather_info import recommands

contents = []
template = {
    "object_type":"list",
    "header_title":"현재 날씨에 따른 음식 추천",
    "header_link":{
        "web_url":weather_url,
        "mobile_web_url":weather_url
    },
    "content":contents,
    "buttons":[
        {
            "title":"날씨 정보 상세 보기",
            "link":{
                "web_url":weather_url,
                "mobile_web_url":weather_url
            }
        }
    ],
}

for place in recommands:
    title = place.get('title')
    title = title.replace("<b>","").replace("</b>","")
    category = place.get('category')
    telephone = place.get('telephone')
    address = place.get('address')









