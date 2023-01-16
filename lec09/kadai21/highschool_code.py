from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import sys

# C0A20047

if __name__ == "__main__":
    driver = webdriver.Chrome("chromedriver")
    driver.maximize_window()
    driver.get("https://www.teu.ac.jp/")

    l = driver.find_element(By.LINK_TEXT, "入試・入学案内")
    l.click()
    sleep(1)
    l = driver.find_element(By.LINK_TEXT, "高校コード検索")
    l.click()
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    driver.find_element(By.ID, "txtKokoNm").click()
    sleep(1)
    search_bar = driver.find_element(By.NAME, "txtKokoNm")
    search_bar.send_keys("東京工業高専")
    sleep(1)
    l = driver.find_element(By.LINK_TEXT, "検索").click()
    sleep(2)
    driver.save_screenshot(sys.argv[1])
