# Selenium을 이용한 크롤러
## Selenium 
- 일반적으로 웹앱을 테스트하는데 이용하는 프레임워크
- 일종의 자동화 프로그램으로 프로그래밍으로 브라우저 동작을 제어해서 마치 사람이 이용하는 것과 같이 웹페이지를 요청하고 응답을 받을 수 있음
- 즉, 로그인이나, 특정 버튼을 누르는 것과 같은 동작을 프로그래밍으로 제어 가능
- webdriver라는 api를 이용해 운영체제에 설치된 브라우저(Chrome, Firefox..)를 제어 가능

    ![Selenium](https://github.com/sw1203/TIL/blob/master/Img/Selenium.PNG)

1. Selenium 설치 방법

```bash
pip install selenium
```

2. webdriver 설치
- Selenium은 webdriver를 통해 설치된 브라우저를 제어하기 때문에 webdriver 설치가 필요
- 디바이스에 설치된 브라우저와 맞는 버전을 설치

    브라우저 | 링크 |
    :------: |:--------------: |
    Chrome | <https://sites.google.com/a/chromium.org/chromedriver/downloads> |
    Edge   | <https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/> |
    Firefox | <https://github.com/mozilla/geckodriver/releases> |
    Safari | <https://webkit.org/blog/6900/webdriver-support-in-safari-10/> |

3. [예제 코드](https://github.com/sw1203/TIL/tree/master/Python/Code/Selenium.py)

```python
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# 다운 받은 Chromedriver의 위치
path = 'D:/chromedriver/chromedriver.exe'

driver = webdriver.Chrome(path)

#Url에 접근 
driver.get('https://www.naver.com')
```

4. 함수
    1. get('URL')
        - URL에 접근하는 api
    2. 탐색 함수
        함수명|설명|
        -----|----|
        find_element_by_id | id로 element 접근 |
        find_element_by_class_name | class로 element 접근|
        find_element_by_name | name으로 element 접근 |
        find_element_by_xpath | xpath를 이용해서 element 접근 |
        - 이외에도 여러 탐색 함수들이 있음

    3. send_keys
        - text의 경우는 값을 전달
        - key 값을 넣으면 동작을 지식
        - [key 값](https://selenium.dev/selenium/docs)
        ```python
        # id라는 name을 가진 element에 'id'라는 값을 전송
        driver.find_element_by_name('id').send_keys('id')
        ```

5. [Naver 지도 검색](https://github.com/sw1203/TIL/tree/master/Python/Code/Selenium.py)

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 다운 받은 Chromedriver의 위치
path = 'D:/chromedriver/chromedriver.exe'

driver = webdriver.Chrome(path)

driver.get('https://map.naver.com/v5/search')

#xpath로 네이버 지도 검색창 접급
elem = driver.find_element_by_xpath('/html/body/app/layout/div[2]/div[2]/div[1]/shrinkable-layout/search-layout/search-box/div/div[1]/div/input')

#검색창에 검색할 qeury 전송
elem.send_keys('왕십리 국밥집')

#naver지도에 검색 버튼이 없어서 enter 역할을 하기 위한것
elem.send_keys(Keys.RETURN)
```
# Reference 
1. [나만의 웹 크롤러 만들기 시리즈](https://beomi.github.io/gb-crawling/)
2. [데이터를 분석하는 문과생, 싸코](https://sacko.tistory.com/13)
3. [명월 일지](https://nowonbun.tistory.com/688)