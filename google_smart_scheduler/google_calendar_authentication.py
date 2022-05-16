
from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build
import datetime


creds_filename = 'res/google_token.json'
SCOPES = ['https://www.googleapis.com/auth/calendar']

flow = InstalledAppFlow.from_client_secrets_file(creds_filename, SCOPES)
creds = flow.run_local_service(port = 0)
service = build('calendar', 'v3', credentials=creds)

today = datetime.datetime.today().strftime("%Y-%m-%d")
# 일정 조회

########################################################################
event = {
    'summary':'오늘 배워 쓰는 API',
    'location':'서울시',
    'description':'API 수업 설명',
    'start':{
        'dateTime':today + 'T09:00:00',
        'timeZone':'Asia/Seoul',
    },
    'end':{
        'dateTime':today + 'T10:00:00',
        'timeZone':'Asia/Seoul',
    },
    'attendees':[
        {'email':'lpage@example.com'},
        {'email':'sbrin@example.com'},
    ],
    'reminders':{
        'useDefault':False,
        'overrides':[
            {'method':'email', 'minutes':24*60},
            {'method':'popup', 'minutes':10},
        ],
    },
}

event = service.events().insert(calendarId='primary', body=event).execute()
print('event created: %s'%(event.get('htmlLink')))


## 일정 조회

calendar_id = 'primary'
today = datetime.date.today().strftime("%Y-%m-%d")

time_min = today + "T00:00:00+09:00"
time_max = today + "T23:59:59+09:00"

max_results = 5
is_single_events = True
orderby='startTime'

events_result = service.events().list(calendarId = calendar_id,
                                      timeMin = time_min,
                                      timeMax = time_max,
                                      maxResults = max_results,
                                      singleEvents = is_single_events,
                                      orderBy = orderby
                                      ).execute()
items = events_result.get('items')
print('==== 일정목록 출력 ====')
print(items)


## 일정 수정

event = events_result.get('items')[0]
event_id = event.get('id')

event['summary'] = '(수정된)'+event['summary']

updated_event = service.events().update(calendarId='primary',
                                        eventId=event_id, body=event).execute()

## 일정 삭제

eventId = updated_event.get('id')
service.events().delete(calendarId='primary', eventId=eventId).execute()


# 카카오톡 활용하기
import json
from kakaoTALK_sending.taking_token import *

KAKAO_TOKEN_FILENAME
KAKAO_APP_KEY = "REST_API 키 입력"
update_tokens(KAKAO_APP_KEY,KAKAO_TOKEN_FILENAME)

gaddr_url = 'https://search.naver.com/search.naver?query='+glocation + ' 맛집'
contents = []

template ={
    'object_type':'list',
    'header_title':gsummary + ' - 맛집추천',
    'header_link':{
        'web_url':gevent_url,
        'mobile_web_url':gevent_url
    },
    'contents':contents,
    'buttons':[
        {
            'title':'일정 자세히 보기',
            'link':{
                'web_url':gevent_url,
                'mobile_web_url':gevent_url
            }
        },
        {
            'title':'일정 장소 보기',
            'link':{
                'web_url':gaddr_url,
                'mobile_web_url':gaddr_url
            }
        }
    ],
}

for place in places:
    ntitle = place.get('title')
    ncategory = place.get('category')
    ntelephone = place.get('telephone')
    nlocation = place.get('address')

    query = nlocation + " "+ntitle

    if '카페' in ncategory:
        image_url = "https://freesvg.org/img/pitr_Coffee_cup_icon.png"
    else:
        image_url = "https://freesvg.org/img/bentolunch.png?2=150&h=150&fit=fill"

    if ntelephone:
        ntitle = ntitle + "\ntel)"+ntelephone

    content = {
        "title":"["+ncategory+"] "+ntitle,
        "description":' '.join(nlocation.split()[1:]),
        "image_url":image_url,
        "image_width":50, "image_height":50,
        "link":{
            "web_url":"https://search.naver.com/search.naver?query=" + query,
            "mobile_web_url":"https://search.naver.com/search.naver?query=" + query
        }
    }
    contents.append(content)

res =

