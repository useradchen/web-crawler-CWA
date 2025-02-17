# pip install selenium

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


def getc(x, a):  # x 為縣市市區 , a 為該縣市地區的編號
    # print("x = " , x)
    url = "https://www.cwb.gov.tw/V8/C/"
    driver = webdriver.Chrome()
    # headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

    driver.get(url)

    driver.set_window_size(1024, 768)

    time.sleep(2)

    # //*[@id="default_map"]/div[3]/a[2]/img 台北(為預設)
    # //*[@id="default_map"]/div[3]/a[3]/img 新北市
    # //*[@id="default_map"]/div[3]/a[4]/img 桃園市
    # //*[@id="default_map"]/div[3]/a[5]/img 新竹縣
    # //*[@id="default_map"]/div[3]/a[6]/img 新竹市

    # 1:基隆市 , 2:台北市 , 3:新北市 , 4:桃園市 , 5:新竹縣 , 6:新竹市 , 7:苗栗縣
    # 8:台中市 , 9:南投縣 , 10:彰化縣 , 11:雲林縣 , 12:嘉義縣 , 13:嘉義市 , 14:台南市
    # 15:高雄市 , 16:屏東縣  , 17:台東縣 , 18:花蓮縣 , 19:宜蘭縣 , 20:澎湖縣 , 21:金門縣 , 22:連江縣
    # //*[@id="default_map"]/div[3]/a[14]/img
    # x = '14'
    if x != 2:
        x = str(x)
        area_path_c = '//*[@id="default_map"]/div[3]/a[' + x + "]/img"
        # 點擊
        time.sleep(1)
        driver.find_element(By.XPATH, area_path_c).click()

    # 下拉式選單元素路徑
    area_path = '//*[@id="home-select-town"]'

    time.sleep(1)

    # 找到下拉式選單元素
    dropdown = Select(driver.find_element(By.XPATH, area_path))

    time.sleep(2)

    # 選擇下拉式選單中的第2個選項
    # a 為使用者輸入的地區
    # a=1
    dropdown.select_by_index(a)

    time.sleep(2)
    # //*[@id="default_map"]/div[3]/a[2]/img

    button_path = '//*[@id="home-form"]/button'  # 確定區域按鈕
    driver.find_element(By.XPATH, button_path).click()

    time.sleep(2)

    week_path = '//*[@id="Tab_weeksTable"]'  # 一周預報
    driver.find_element(By.XPATH, week_path).click()

    time.sleep(3)

    # # 往下滑動
    # #driver.execute_script("window.scrollTo(0 , document.body.scrollHeight);")

    # element = driver.find_element_by_id('#PC3_Wx')
    # element.location_once_scrolled_into_view

    # time.sleep(3)
    # TableIdweeks > tbody > tr:nth-child(3) > td:nth-child(2) > span.tem-C.is-active

    t_all = []  # 溫度
    date = []  # 日期
    # //*[@id="PC7_D7"]
    # i 為區域編號
    for i in range(1, 8):
        i = str(i)
        d_selector_1 = "#PC7_D" + i  # 日期星期位置
        d_p_1 = driver.find_element(By.CSS_SELECTOR, d_selector_1).text.split("\n")
        date.append(d_p_1)

    # print("date = " , date)
    # print()

    # TableIdweeks > tbody > tr:nth-child(3) > td:nth-child(2) > span.tem-C.is-active
    # TableIdweeks > tbody > tr:nth-child(3) > td:nth-child(4) > span.tem-C.is-active
    # TableIdweeks > tbody > tr:nth-child(3) > td:nth-child(6) > span.tem-C.is-active

    # j 為溫度編號
    for j in range(2, 15, 2):
        j = str(j)
        t_selector_1 = ("#TableIdweeks > tbody > tr:nth-child(3) > td:nth-child("+ j+ ") > span.tem-C.is-active")
        t_p = driver.find_element(By.CSS_SELECTOR, t_selector_1).text
        #    print("溫度 = "  , t_p)
        t_all.append(t_p)
    # print("t_all = " , t_all)

    time.sleep(1)

    # 當日降雨機率
    rain_selector = "#TableIdweeks > tbody > tr:nth-child(5) > td:nth-child(2)"

    time.sleep(1)

    r_p = driver.find_element(By.CSS_SELECTOR, rain_selector).text
    # print('r_p = ' , r_p)

    time.sleep(3)

    driver.close()
    return t_all, date, r_p


# ans = getc(2, 3)
# print(ans)
