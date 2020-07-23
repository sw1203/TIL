# BeautifulSoup & request를 이용한 웹 크롤러
## 웹 크롤러란?
- 방대한 웹 페이지를 방문하며, 각종 정보를 자동적으로 수집하는 일을 하는 프로그램

## Requests
- Python에서 HTTP 요청을 보내는 라이브러리
1. 설치 방법

```bash
pip install requests
```

2. 예제코드

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