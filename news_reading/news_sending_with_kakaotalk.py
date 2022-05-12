
import json
from kakaoTALK_sending.taking_token import update_tokens, send_message

KAKAO_TOKEN_FILENAME='res/kakao_token.json'
KAKAO_APP_KEY = 'REST_API키 입력'
update_tokens(KAKAO_APP_KEY, KAKAO_TOKEN_FILENAME)

sections_ko = {'pol':'정치', 'eco':'경제','soc':'사회'}

navernews_url = "https://news.naver.com/main/home.nhn"

contents = []

template = {
    "object_type":"list",
    "header_title":sections_ko[my_section] + "분야 상위 뉴스 빅3",
    "header_link":{
        "web_url":navernews_url,
        "mobile_web_url":navernews_url
    },
    "contents":contents,
    "button_title":"네이버 뉴스 바로가기"
}
for news_info in news_list3:
    content = {
        "title":news_info.get('title'),
        "description":"작성일 : "+ news_info.get('date'),
        "image_url":news_info.get('image_url'),
        "image_width":50,
        "image_height":50,
        "link":{
            "web_url":news_info.get('news_url'),
            "mobile_web_url":news_info.get('news_url')
        }
    }
    contents.append(content)

res= send_message(KAKAO_TOKEN_FILENAME, template)



######################################################
# 위 코드 외에 텍스트 템플릿으로 보내는 코드

for ids, news_info in enumerate(news_list3):
    template = {
        "object_type":"text",
        "text":"#제목 :" + news_info.get('title')+'\n\n# 요약 : ' + news_info.get('snews_contents'),
        "link":{
            "web_url":news_info.get('news_url'),
            'mobile_web_url':news_info.get('news_url')
        },
        'button_title':'자세히 보기'
    }

    res = send_message(KAKAO_TOKEN_FILENAME, template)
    if res.json().get('result_code') == 0:
        print('뉴스를 성공적으로 보냈습니다.')
    else:
        print('뉴스를 성공적으로 보내지 못했습니다. 오류메시지 : ', res.json())


