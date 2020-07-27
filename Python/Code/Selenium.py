import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# 다운 받은 Chromedriver의 위치
path = 'D:/chromedriver/chromedriver.exe'

driver = webdriver.Chrome(path)

#Url에 접근 
driver.get('https://www.naver.com')