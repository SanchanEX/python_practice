from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

if __name__ == "__main__":
    driver = webdriver.Chrome("chromedriver")
    driver.maximize_window() #ウインドウ最大化
    driver.get("https://www.teu.ac.jp/")
    print(driver.title) # ページタイトル

    #link = driver.find_element(by=By.CLASS_NAME, value="gakubu")
    link = driver.find_element(By.LINK_TEXT, "学部･大学院案内")
    link.click()
    sleep(5)
