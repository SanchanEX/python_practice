from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import sys

# C0A20047

if __name__ == "__main__":
    driver = webdriver.Chrome("chromedriver")
    driver.maximize_window()
    driver.get("https://www.teu.ac.jp/")

    link = driver.find_element(By.LINK_TEXT, "交通案内")
    link.click()
    sleep(1)
    link = driver.find_element(
        By.LINK_TEXT, "2022年度スクールバス運行時刻表《月～金曜日運行》(2022年4月7日（木）より運行)2022年4月14日更新")
    link.click()
    link = driver.find_element(By.LINK_TEXT, "八王子駅南口行")
    link.click()
    sleep(2)
    driver.save_screenshot(sys.argv[1])
