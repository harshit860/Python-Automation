from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitterbot:
    def __init__(self,username,password):
        self.username = username
        self.password = password 
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.facebook.com/')
        time.sleep(3)
        email = bot.find_element_by_id('email')
        password = bot.find_element_by_id('pass')
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

harshit = Twitterbot('username','password')
harshit.login()