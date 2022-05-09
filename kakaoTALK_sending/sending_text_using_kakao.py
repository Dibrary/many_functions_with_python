import json
import requests
from taking_token import load_tokens

KAKAO_TOKEN_FILENAME = "res/kakao_token.json"

tokens = load_tokens(KAKAO_TOKEN_FILENAME)

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

headers = {
    "Authorization":"Bearer " + tokens['access_token']
}

data = {
    "template_object":json.dumps({"object_type":"text",
                                  "text":"Hello, World",
                                  "link": {
                                      "web_url":"www.naver.com"
                                  }
    })
}

response = requests.post(url, headers=headers, data = data)
print(response.status_code)

if response.status_code != 200:
    print("Error", response.json())
else:
    print("성공으로 보냈습니다.")

# 보내는데 성공함.