import requests
import json

url = "https://dapi.kakao.com/v2/search/image"
headers={
    "Authorization":"KakaoAK <REST_API APP key ENTER>" # KakaoAK와 앱키 사이에 한개의 공백 존재.
}
data = {
    "query":"펭수"
}

response = requests.post(url, headers=headers, data=data)
if response.status_code != 200:
    print("Error", response.json())
else:
    count = 0
    for image_info in response.json()["documents"]:
        print(f'[{count}th] image_url = ', image_info['image_url'])
        count += 1

