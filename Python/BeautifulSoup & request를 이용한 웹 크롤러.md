# BeautifulSoup & request를 이용한 웹 크롤러
## 웹 크롤러란?
- 방대한 웹 페이지를 방문하며, 각종 정보를 자동적으로 수집하는 일을 하는 프로그램

## Requests
- Python에서 HTTP 요청을 보내는 라이브러리
1. 설치 방법

```bash
pip install requests
```

2. 예제 코드

```python
import requests

# HTTP GET Request
req = requests.get('https://www.daum.net/')

#HTML 소스 가져오기
html = req.text

#HTML Header 가져오기
header = req.headers

#HTML Status 가져오기 (200: 정상)
status = req.status_code

print(html)
```

- html을 Python이 이해하는 객체 구조로 만들어 주지는 못함
- req.text는 문자열 객체를 반환하여 우리가 원하는 정보를 추출하기 어려움

## BeautifulSoup
- HTML이나 xml 파일을 Python이 이해하는 객체 구조로 변환하는 역할
- 즉, HTML과 XML 파일에서 데이터를 꺼내기 위한 파이썬 라이브러리

1. 설치 방법

```bash
pip install beautifulsoup4
```

2. [예제 코드](https://github.com/sw1203/TIL/tree/master/Python/Code/parser.py)
```python
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
my_title = soup.select('div > p')

# p 태그 속성들은 제외하고 텍스트만 가져오기
# 텍스트가 없는 경우도 존재함으로 if문으로 있는 경우만 출력
for title in my_title:
    if title.string is not None:
        print(title.string)
```

3. 함수
    1. find
        - 해당 조건에 맞는 태그 가져오기
        - 조건에 맞는 값이 여러개인 경우 첫 번째 태그 가져오기
        ```python
        bs.find('div') # 최초 검색 된 div 태그 값 가져오기

        bs.find('div',{'id':'shin'}) # div 태그에서 id 속성 값이 shin인거 찾기
        ```
    2. find_all
        - 해당 조건에 맞는 모든 태그 가져오기
        ```python
        bs.find_all('a') # 모든 a 태그 검색 soup('a')와 도일

        bs.find_all('a',limit=2) # a 태그를 두개만 가져옴

        bs.find_all(align='center') # 속성 값을 기준으로 태그 읽기

        bs.find_all(['p','img']) # 'p'나 'img' 태그 읽기
        ```
    - 이외에도 다양한 함수가 있고 사용법이 있음

# Reference 
1. [나만의 웹 크롤러 만들기 시리즈](https://beomi.github.io/gb-crawling/)
2. [아무튼 워라벨](http://hleecaster.com/python-web-crawling-with-beautifulsoup/)
3. [TWpower's Tech Blog](https://twpower.github.io/84-how-to-use-beautiful-soup)
4. [Gamja's Farm](https://sang-gamja.tistory.com/142)
5. [w3schools](https://www.w3schools.com/python/module_requests.asp)
6. [BeautifulSoup Documetation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)