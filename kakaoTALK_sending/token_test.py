
import requests as rq

# 파일명을 token 으로 하면 안 됨.

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type":"authorization_code",
    "client_id":"REST API 는 비밀",
    "redirect_uri":"https://localhost.com",
    "code":"코드는 비밀" # 발급받은 인증코드 사용
}

response=rq.post(url, data=data)

if response.status_code != 200:
    print("Error", response.json())
else:
    tokens = response.json()
    print(tokens)

# 발급받은 인증 코드로 토큰을 발급받는 것은 1번만 가능. 다시 하려면 코드 값을 재발급 받아야 한다.


