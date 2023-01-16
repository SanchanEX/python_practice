from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

if __name__ == "__main__":
    driver = webdriver.Chrome("chromedriver")
    driver.maximize_window() #ウインドウ最大化
    driver.get("https://www.teu.ac.jp/")

