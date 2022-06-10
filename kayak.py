import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "https://www.kayak.pl/flights"
driver = webdriver.Chrome(
    executable_path="D:\Program Files (x86)\chromedriver\chromedriver.exe"
)
driver.maximize_window()


def closeCookie():
    cookieButton = driver.find_elements(by=By.XPATH, value="//button[@role='button']")
    print(cookieButton)
    time.sleep(1)
    cookieButton[7].click()


def dep_country_chooser(dep_country):
    remove_default = driver.find_element(
        by=By.XPATH, value="//div[@class='vvTc-item-close']"
    )
    time.sleep(1)
    remove_default.click()
    fly_from = driver.find_element(by=By.XPATH, value="//input[@aria-label='Wylot z']")
    time.sleep(1)
    fly_from.click()
    time.sleep(1)
    fly_from.clear()
    time.sleep(1)
    fly_from.click()
    time.sleep(1.5)
    fly_from.send_keys(dep_country)


def ret_country_chooser(ret_country):
    fly_from = driver.find_element(
        by=By.XPATH, value="//input[@aria-label='Kierunek podróży']"
    )
    time.sleep(1)
    fly_from.click()
    time.sleep(1.5)
    fly_from.send_keys(ret_country)


def dep_date_chooser(dep_date):
    date_box = driver.find_element(by=By.XPATH, value="//span[@class='sR_k-value']")
    time.sleep(1)
    date_box.click()
    time.sleep(5.5)
    date_button = driver.find_element(
        by=By.XPATH, value="//div[@aria-label='13 lip 2022']"
    )
    date_button.click()


def ret_date_chooser(ret_date):
    time.sleep(1)
    date_button = driver.find_element(
        by=By.XPATH, value="//div[@aria-label='21 lip 2022']"
    )
    date_button.click()


def submit_search():
    sub_button = driver.find_element(
        by=By.XPATH, value="//button[@aria-label='Szukaj']"
    )
    print(sub_button)
    time.sleep(1)
    sub_button.click()


def load_more():
    more_button = driver.find_element(by=By.XPATH, value="//a[@class='moreButton']")
    time.sleep(1)
    more_button.click()


def cheapest_results():
    cheap_button = driver.find_element(by=By.XPATH, value="//a[@data-sort='price_a']")
    time.sleep(1)
    cheap_button.click()


def best_results():
    best_button = driver.find_element(
        by=By.XPATH, value="//a[@data-sort='bestflight_a']"
    )
    time.sleep(1)
    best_button.click()


def get_flight_data():
    dep_time_1 = driver.find_element(
        by=By.XPATH, value="//span[@class='depart-time base-time']"
    )
    print(dep_time_1.text)
    time.sleep(15)


def process_results():
    get_flight_data()
    time.sleep(15)
    cheapest_results()
    time.sleep(5)
    best_results()
    time.sleep(5)
    load_more()
    time.sleep(5)
    load_more


driver.get(link)
time.sleep(5)
closeCookie()
time.sleep(random.uniform(0.5, 2))
dep_country_chooser("krk")
time.sleep(random.uniform(0.5, 2))
ret_country_chooser("lon")
time.sleep(random.uniform(0.5, 2))
dep_date_chooser(1)
time.sleep(random.uniform(0.5, 2))
ret_date_chooser(1)
time.sleep(random.uniform(0.5, 2))
submit_search()
time.sleep(30)
process_results()
time.sleep(20)


driver.quit()
