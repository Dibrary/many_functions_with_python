import requests
import json

def save_image(image_url, file_name):
    img_response = requests.get(image_url)
    if img_response.status_code == 200:
        with open("images/"+file_name, "wb") as fp:
            fp.write(img_response.content)

url = "https://dapi.kakao.com/v2/search/image"
headers={
    "Authorization":"KakaoAK <REST_API APP key ENTER>" # 한글로 하면 Latin 에러 남.
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
        file_name = "test_%d.jpg"%(count)
        save_image(image_info['image_url'], file_name)





