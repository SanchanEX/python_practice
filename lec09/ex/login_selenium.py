from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

if __name__ == "__main__":
    options = Options()
    options.add_argument(r"--user-data-dir=C:\Users\admin\AppData\Local\Google\Chrome\User Data")
    options.add_argument(r"--profile-directory=Profile 1")
    driver = webdriver.Chrome("chromedriver", options=options)
    driver.maximize_window() #ウインドウ最大化
    driver.get("https://service.cloud.teu.ac.jp/moodle_epyc/course/view.php?id=9907")
    driver.find_element(By.XPATH, "//span[text()='自動提出']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//a[@title='追加 ...']").click()
    sleep(1)
    upload = driver.find_element(By.XPATH, "//input[@type='file']")
    upload.send_keys(r"C:\Users\admin\Desktop\ProA2\lec09\login_selenium.py")
    driver.find_element(By.XPATH, "//button[text()='このファイルをアップロードする']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    sleep(5)
    