from selenium import webdriver
from bs4 import BeautifulSoup

# Edge
driver = webdriver.Edge()

# Loading
driver.get("https://www.cwa.gov.tw/V8/C/E/index.html")

# delay
driver.implicitly_wait(3) 

# get source
html = driver.page_source

# quit
driver.quit()

# 解析 HTML
soup = BeautifulSoup(html, "html.parser")

for i in range(1,4):
    eq_row = soup.find('tr', id=f'eq-{i}')

    if eq_row:
        area = eq_row.find('td', headers='num').text.strip()
        eq_level = eq_row.find('td', class_='eq_lv-1').text.strip()
        eq_detail = eq_row.find('div', class_='eq-detail')
        eq_time = eq_detail.find('span').text.strip()
        location = eq_detail.find('ul').find('li').text.strip()

        print("小區域:", area)
        print("地震等級:", eq_level)
        print("地震時間和動態:", eq_time)
        print("地震地點:", location)
    else:
        print("沒有找到地震訊息。")
   