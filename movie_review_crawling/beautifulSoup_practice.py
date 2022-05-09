from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<a href ="http://example.com/elsie" class="sister" id="link1">Elsie</a>
"""

soup = BeautifulSoup(html_doc,"lxml")
print("soup.body.p 결과", soup.body.p, "\n")
print(soup)
print("\n")
print(soup.head.title, " \nstring결과 = ",soup.head.title.string) # string을 써 줘야 해당 내용이 나온다.
print("\n")
print(soup.contents) # 리스트로 반환된다.
print("\n")
print(soup.contents[0]) # 이렇게 까지는 할 수 있으나 2차 슬라이싱 불가능.
print("\n=====================================================")
for idx, k in enumerate(soup.contents[0]):
    print(idx, k)
