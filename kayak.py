import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd


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
    remove_default.click()
    fly_from = driver.find_element(by=By.XPATH, value="//input[@aria-label='Wylot z']")
    time.sleep(random.uniform(0.3, 1))
    fly_from.click()
    time.sleep(random.uniform(0.3, 1))
    fly_from.clear()
    time.sleep(random.uniform(0.3, 1))
    fly_from.click()
    time.sleep(random.uniform(0.3, 1))
    fly_from.send_keys(dep_country)


def ret_country_chooser(ret_country):
    fly_from = driver.find_element(
        by=By.XPATH, value="//input[@aria-label='Kierunek podróży']"
    )
    fly_from.click()
    time.sleep(random.uniform(0.3, 1))
    fly_from.send_keys(ret_country)


def dep_date_chooser(dep_date):
    date_box = driver.find_element(by=By.XPATH, value="//span[@class='sR_k-value']")
    date_box.click()
    time.sleep(5)
    date_button = driver.find_element(
        by=By.XPATH, value="//div[@aria-label='18 lip 2022']"
    )
    date_button.click()


def ret_date_chooser(ret_date):
    date_button = driver.find_element(
        by=By.XPATH, value="//div[@aria-label='29 lip 2022']"
    )
    date_button.click()


def submit_search():
    sub_button = driver.find_element(
        by=By.XPATH, value="//button[@aria-label='Szukaj']"
    )
    sub_button.click()


def load_more():
    more_button = driver.find_element(by=By.XPATH, value="//a[@class='moreButton']")
    more_button.click()


def cheapest_results():
    cheap_button = driver.find_element(by=By.XPATH, value="//a[@data-sort='price_a']")
    cheap_button.click()


def best_results():
    best_button = driver.find_element(
        by=By.XPATH, value="//a[@data-sort='bestflight_a']"
    )
    best_button.click()


def get_flight_data(index, index4, index8, df):

    print("\n" + "result " + str(index + 1) + "\n")

    # flight 1
    print("flight 1:")
    dep_time_1 = driver.find_elements(
        by=By.XPATH, value="//span[@class='depart-time base-time']"
    )
    print(dep_time_1[index4].text)

    arr_time_1 = driver.find_elements(
        by=By.XPATH, value="//span[@class='arrival-time base-time']"
    )
    print(arr_time_1[index4].text)

    airport_1 = driver.find_elements(by=By.XPATH, value="//span[@class='airport-name']")
    print(airport_1[index8].text)

    airport_2 = driver.find_elements(by=By.XPATH, value="//span[@class='airport-name']")
    print(airport_2[index8 + 1].text)

    stops_1 = driver.find_elements(
        by=By.XPATH, value="//span[contains(@class,'stops-text')]"
    )
    print(stops_1[index4].text)

    time_1 = driver.find_elements(
        by=By.XPATH,
        value="//div[contains(@class,'duration') and contains(@class,'section')]/*[1]",
    )
    print(time_1[index4].text)

    # flight 2
    print("flight 2:")
    dep_time_1 = driver.find_elements(
        by=By.XPATH, value="//span[@class='depart-time base-time']"
    )
    print(dep_time_1[index4 + 1].text)

    arr_time_1 = driver.find_elements(
        by=By.XPATH, value="//span[@class='arrival-time base-time']"
    )
    print(arr_time_1[index4 + 1].text)

    airport_1 = driver.find_elements(by=By.XPATH, value="//span[@class='airport-name']")
    print(airport_1[index8 + 2].text)

    airport_2 = driver.find_elements(by=By.XPATH, value="//span[@class='airport-name']")
    print(airport_2[index8 + 3].text)

    stops_1 = driver.find_elements(
        by=By.XPATH, value="//span[contains(@class,'stops-text')]"
    )
    print(stops_1[index4 + 1].text)

    time_1 = driver.find_elements(
        by=By.XPATH,
        value="//div[contains(@class,'duration') and contains(@class,'section')]/*[1]",
    )
    print(time_1[index4 + 1].text)

    # airlines
    airlines = driver.find_elements(
        by=By.XPATH, value="//span[@class='codeshares-airline-names']"
    )
    print(airlines[index].text)

    # price
    price = driver.find_elements(by=By.XPATH, value="//span[@class='price-text']")
    print(price[index].text)
    time.sleep(1)


def get_flight_data1(index, index4, index8, df):

    l = list()
    print("\n" + "result " + str(index + 1) + "\n")

    # flight 1
    print("flight 1:")
    dep_time_1 = driver.find_elements(
        by=By.XPATH, value="//span[@class='depart-time base-time']"
    )
    print(dep_time_1[index4].text)
    l.append(dep_time_1[index4].text)

    arr_time_1 = driver.find_elements(
        by=By.XPATH, value="//span[@class='arrival-time base-time']"
    )
    print(arr_time_1[index4].text)
    l.append(arr_time_1[index4].text)

    airport_1 = driver.find_elements(by=By.XPATH, value="//span[@class='airport-name']")
    print(airport_1[index8].text)
    l.append(airport_1[index8].text)

    airport_2 = driver.find_elements(by=By.XPATH, value="//span[@class='airport-name']")
    print(airport_2[index8 + 1].text)
    l.append(airport_2[index8 + 1].text)

    stops_1 = driver.find_elements(
        by=By.XPATH, value="//span[contains(@class,'stops-text')]"
    )
    print(stops_1[index4].text)
    l.append(stops_1[index4].text)

    time_1 = driver.find_elements(
        by=By.XPATH,
        value="//div[contains(@class,'duration') and contains(@class,'section')]/*[1]",
    )
    print(time_1[index4].text)
    l.append(time_1[index4].text)

    # flight 2
    print("flight 2:")
    dep_time_1 = driver.find_elements(
        by=By.XPATH, value="//span[@class='depart-time base-time']"
    )
    print(dep_time_1[index4 + 1].text)
    l.append(dep_time_1[index4 + 1].text)

    arr_time_1 = driver.find_elements(
        by=By.XPATH, value="//span[@class='arrival-time base-time']"
    )
    print(arr_time_1[index4 + 1].text)
    l.append(arr_time_1[index4 + 1].text)

    airport_1 = driver.find_elements(by=By.XPATH, value="//span[@class='airport-name']")
    print(airport_1[index8 + 2].text)
    l.append(airport_1[index8 + 2].text)

    airport_2 = driver.find_elements(by=By.XPATH, value="//span[@class='airport-name']")
    print(airport_2[index8 + 3].text)
    l.append(airport_2[index8 + 3].text)

    stops_1 = driver.find_elements(
        by=By.XPATH, value="//span[contains(@class,'stops-text')]"
    )
    print(stops_1[index4 + 1].text)
    l.append(stops_1[index4 + 1].text)

    time_1 = driver.find_elements(
        by=By.XPATH,
        value="//div[contains(@class,'duration') and contains(@class,'section')]/*[1]",
    )
    print(time_1[index4 + 1].text)
    l.append(time_1[index4 + 1].text)

    # airlines
    airlines = driver.find_elements(
        by=By.XPATH, value="//span[@class='codeshares-airline-names']"
    )
    print(airlines[index].text)
    l.append(airlines[index].text)

    # price
    price = driver.find_elements(by=By.XPATH, value="//span[@class='price-text']")
    print(price[index].text)
    l.append(price[index].text)
    time.sleep(1)

    print(l)
    df.loc[df.shape[0]] = l


def process_results():

    columns = (
        "dep_time_1",
        "arr_time_1",
        "airport_1_1",
        "airport_1_2",
        "stops_1",
        "time_1",
        "dep_time_2",
        "arr_time_2",
        "airport_2_1",
        "airport_2_2",
        "stops_2",
        "time_2",
        "airlines",
        "prize",
    )
    df = pd.DataFrame(columns=columns)
    print(df)

    cheapest_results()
    time.sleep(5)
    index = 0
    index4 = 0
    index8 = 0

    while index < 15:
        get_flight_data(index, index4, index8)
        index += 1
        index4 += 4
        index8 += 8
    load_more()
    time.sleep(5)

    while index < 30:
        get_flight_data(index, index4, index8)
        index += 1
        index4 += 4
        index8 += 8
    load_more()
    time.sleep(5)

    while index < 45:
        get_flight_data(index, index4, index8)
        index += 1
        index4 += 4
        index8 += 8
    load_more()
    time.sleep(5)

    time.sleep(500)


driver.get(link)
time.sleep(10)
closeCookie()
time.sleep(random.uniform(0.5, 2))
dep_country_chooser("waw")
time.sleep(random.uniform(0.5, 2))
ret_country_chooser("tos")
time.sleep(random.uniform(0.5, 2))
dep_date_chooser(1)
time.sleep(random.uniform(0.5, 2))
ret_date_chooser(1)
time.sleep(random.uniform(0.5, 2))
submit_search()
time.sleep(30)
# process_results()

columns = (
    "dep_time_1",
    "arr_time_1",
    "airport_1_1",
    "airport_1_2",
    "stops_1",
    "time_1",
    "dep_time_2",
    "arr_time_2",
    "airport_2_1",
    "airport_2_2",
    "stops_2",
    "time_2",
    "airlines",
    "prize",
)
df = pd.DataFrame(columns=columns)
print(df)
get_flight_data1(0, 0, 0, df)
print(df)
time.sleep(20)


driver.quit()
