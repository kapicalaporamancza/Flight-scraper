import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import openpyxl
from datetime import datetime
import email_send



def closeCookie(driver):
    cookieButton = driver.find_elements(by=By.XPATH, value="//button[@role='button']")
    time.sleep(1)
    cookieButton[7].click()


def dep_country_chooser(dep_country, driver):
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


def ret_country_chooser(ret_country, driver):
    fly_from = driver.find_element(
        by=By.XPATH, value="//input[@aria-label='Kierunek podróży']"
    )
    fly_from.click()
    time.sleep(random.uniform(0.3, 1))
    fly_from.send_keys(ret_country)


def dep_date_chooser(dep_date, driver):
    date_box = driver.find_element(by=By.XPATH, value="//span[@class='sR_k-value']")
    date_box.click()
    time.sleep(5)
    path = "//div[@aria-label='" + dep_date + "']"
    date_button = driver.find_element(
        by=By.XPATH, value=path
    )
    date_button.click()


def ret_date_chooser(ret_date, driver):
    path = "//div[@aria-label='" + ret_date + "']"
    date_button = driver.find_element(
        by=By.XPATH, value=path)
    date_button.click()


def submit_search(driver):
    sub_button = driver.find_element(
        by=By.XPATH, value="//button[@aria-label='Szukaj']"
    )
    sub_button.click()


def load_more(driver):
    more_button = driver.find_element(by=By.XPATH, value="//a[@class='moreButton']")
    more_button.click()


def cheapest_results(driver):
    cheap_button = driver.find_element(by=By.XPATH, value="//a[@data-sort='price_a']")
    cheap_button.click()


def best_results(driver):
    best_button = driver.find_element(
        by=By.XPATH, value="//a[@data-sort='bestflight_a']"
    )
    best_button.click()


def get_flight_data(index, index4, index8, df, driver):

    l = list()

    # flight 1
    dep_time_1 = driver.find_elements(
        by=By.XPATH, value="//span[@class='depart-time base-time']"
    )
    l.append(dep_time_1[index4].text)

    arr_time_1 = driver.find_elements(
        by=By.XPATH, value="//span[@class='arrival-time base-time']"
    )
    l.append(arr_time_1[index4].text)

    airport_1 = driver.find_elements(by=By.XPATH, value="//span[@class='airport-name']")
    l.append(airport_1[index8].text)

    airport_2 = driver.find_elements(by=By.XPATH, value="//span[@class='airport-name']")
    l.append(airport_2[index8 + 1].text)

    stops_1 = driver.find_elements(
        by=By.XPATH, value="//span[contains(@class,'stops-text')]"
    )
    l.append(stops_1[index4].text)

    time_1 = driver.find_elements(
        by=By.XPATH,
        value="//div[contains(@class,'duration') and contains(@class,'section')]/*[1]",
    )
    l.append(time_1[index4].text)

    # flight 2
    dep_time_1 = driver.find_elements(
        by=By.XPATH, value="//span[@class='depart-time base-time']"
    )
    l.append(dep_time_1[index4 + 1].text)

    arr_time_1 = driver.find_elements(
        by=By.XPATH, value="//span[@class='arrival-time base-time']"
    )
    l.append(arr_time_1[index4 + 1].text)

    airport_1 = driver.find_elements(by=By.XPATH, value="//span[@class='airport-name']")
    l.append(airport_1[index8 + 2].text)

    airport_2 = driver.find_elements(by=By.XPATH, value="//span[@class='airport-name']")
    l.append(airport_2[index8 + 3].text)

    stops_1 = driver.find_elements(
        by=By.XPATH, value="//span[contains(@class,'stops-text')]"
    )
    l.append(stops_1[index4 + 1].text)

    time_1 = driver.find_elements(
        by=By.XPATH,
        value="//div[contains(@class,'duration') and contains(@class,'section')]/*[1]",
    )
    l.append(time_1[index4 + 1].text)

    # airlines
    airlines = driver.find_elements(
        by=By.XPATH, value="//span[@class='codeshares-airline-names']"
    )
    l.append(airlines[index].text)

    # price
    price = driver.find_elements(by=By.XPATH, value="//span[@class='price-text']")
    l.append(price[index].text)

    df.loc[df.shape[0]] = l


def process_results(driver, file_name):

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
    
    cheapest_results(driver)
    time.sleep(5)
    index = 0
    index4 = 0
    index8 = 0

    while index < 15:
        get_flight_data(index, index4, index8, df, driver)
        index += 1
        index4 += 4
        index8 += 8
    load_more(driver)
    time.sleep(5)

    while index < 30:
        get_flight_data(index, index4, index8, df, driver)
        index += 1
        index4 += 4
        index8 += 8
    load_more(driver)
    time.sleep(5)

    """while index < 45:
        get_flight_data(index, index4, index8, df, driver)
        index += 1
        index4 += 4
        index8 += 8 """

    df.to_excel(file_name, sheet_name="sheet1")

def process_date(date):
    #d = datetime.strptime(date, "%Y-%m-%d")
    dict_month = {1: "sty", 2: "lut", 3: "mar", 4: "kwi", 5: "Maj", 6: "cze", 7: "lip", 8: "sie", 9: "wrz", 10: "paź", 11: "lis", 12: "gru"}
    return str('{:02d}'.format(date.day)) + " " + dict_month[date.month] + " " + str(date.year)

def proceed_search(driver, dep_country, ret_country, dep_date, ret_date):
    closeCookie(driver)
    time.sleep(random.uniform(0.5, 2))
    dep_country_chooser(dep_country, driver)
    time.sleep(random.uniform(0.5, 2))
    ret_country_chooser(ret_country, driver)
    time.sleep(random.uniform(0.5, 2))
    dep_date_chooser(process_date(dep_date), driver)
    time.sleep(random.uniform(0.5, 2))
    ret_date_chooser(process_date(ret_date), driver)
    time.sleep(random.uniform(0.5, 2))
    submit_search(driver)
    time.sleep(30)
    file_name = dep_country + "_" + ret_country + "_" + dep_date.strftime("%y-%m-%d") + "_" + ret_date.strftime("%y-%m-%d")
    actual_time = datetime.now().strftime("%y-%m-%d-%H-%M")
    file_name = file_name + " " + actual_time + ".xlsx"
    process_results(driver, file_name)
    email_send.sender("Wynik wyszukiwania: " + actual_time, file_name)
    driver.quit()



def search_button(dep_country, ret_country, dep_date, ret_date):
    i = 0
    b = True
    while(i<5 and b):
        try:
            link = "https://www.kayak.pl/flights"
            driver = webdriver.Chrome(executable_path="D:\Program Files (x86)\chromedriver\chromedriver.exe")
            driver.maximize_window()
            driver.get(link)
            time.sleep(10)        
            proceed_search(driver, dep_country, ret_country, dep_date, ret_date)
            b=False
            
        except Exception as e: 
            driver.quit()
            print(e)
        i+=1
