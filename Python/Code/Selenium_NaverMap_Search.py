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



