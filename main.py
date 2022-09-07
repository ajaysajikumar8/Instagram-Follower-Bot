import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "E:\chromedriver_win32\chromedriver.exe"
URL = "https://www.instagram.com/"
SIMILAR_ACCOUNT = "itsbrand_hub"
USER_NAME = ""
PASSWORD = ""


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.maximize_window()

    def login(self):
        self.driver.get(url=f"{URL}/accounts/login/")
        time.sleep(3)
        user_name = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        user_name.send_keys(USER_NAME)
        password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        time.sleep(1)
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(10)
        try:
            notifications_disable = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        except:
            print("Popup Box not found")
        else:
            notifications_disable.click()
        finally:
            print("login successful")

        

    def find_followers(self):
        self.driver.get(url=f"{URL}/{SIMILAR_ACCOUNT}/")
        time.sleep(6)
        following = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[3]/a')
        following.click()
        print("followers found")

    def follow(self):
        print("accounts followed !!")


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
