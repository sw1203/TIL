import requests
from bs4 import BeautifulSoup

# HTTP GET Request
req = requests.get('https://github.com/sw1203')

#HTML 소스 가져오기
html = req.text

#HTML Header 가져오기
header = req.headers

#HTML Status 가져오기 (200: 정상)
status = req.status_code

# BeautifulSoup로 html 소스를 python 객체로 변환하기
# 첫 번째 인자는 변환할 html 소스코드, 두 번째 인자는 어떤 parser를 이용할 것인지
soup = BeautifulSoup(html,'html.parser')

#div 태그 아래에 있는 p 태그 가져오기
title = soup.select('div > p')

# p 태그 속성들은 제외하고 텍스트만 가져오기
# 텍스트가 없는 경우도 존재함으로 if문으로 있는 경우만 출력
for ti in title:
    if ti.string is not None:
        print(ti.string)