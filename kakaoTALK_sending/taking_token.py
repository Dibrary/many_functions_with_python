
import json
import requests
import datetime
import os


# 토큰을 파일로 관리할 수 있는 코드

KAKAO_TOKEN_FILENAME = "res/kakao_token.json"

def save_tokens(filename, tokens):
    with open(filename, "w") as fp:
        json.dump(tokens, fp)

def load_tokens(filename):
    with open(filename) as fp:
        tokens = json.load(fp)

    return tokens

def update_tokens(app_key, filename):
    tokens = load_tokens(filename)

    url = "https://kauth.kakao.com/oauth/token"
    data={
        "grant_type":"refresh_token",
        "client_id":app_key,
        "refresh_token":tokens['refresh_token']
    }
    response = requests.post(url, data=data)

    if response.status_code != 200:
        print("Error", response.json())
        tokens = None
    else:
        print(response.json())
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = filename+"."+now
        os.rename(filename, backup_filename)

        tokens['access_token'] = response.json()['access_token']
        save_tokens(filename, tokens)
    return tokens

def send_message(filename, template):
    tokens = load_tokens(filename)
    headers={
        "Authorization":"Bearer"+tokens['access_token']
    }
    payload = {
        "template_object":json.dumps(template)
    }
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    res = requests.post(url, data=payload, headers=headers)

    return res

tokens = "토큰은 비밀"
save_tokens(KAKAO_TOKEN_FILENAME, tokens)



