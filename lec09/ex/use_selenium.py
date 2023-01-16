from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import sleep

if __name__ == "__main__":
    service = Service(executable_path="chromedriver")
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.teu.ac.jp")
    sleep(10)
