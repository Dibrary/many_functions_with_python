
import requests

url = "https://search1.kakaocdn.net/argon/600x0_65_wr/ImZk3b2X1w8"

img_response = requests.get(url) # 해당 url로 서버에 요청

if img_response.status_code == 200:
    with open("images/test.jpg", "wb") as fp:
        fp.write(img_response.content)


