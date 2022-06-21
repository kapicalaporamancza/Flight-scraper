import random
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
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



def process_date(date):
    dict_month = {1: "sty", 2: "lut", 3: "mar", 4: "kwi", 5: "Maj", 6: "cze", 7: "lip", 8: "sie", 9: "wrz", 10: "paź", 11: "lis", 12: "gru"}
    return str('{:02d}'.format(date.day)) + " " + dict_month[date.month] + " " + str(date.year)


def dep_date_chooser(dep_date, driver):
    date_box = driver.find_element(by=By.XPATH, value="//span[@class='sR_k-value']")
    date_box.click()
    time.sleep(5)

    calendar_dict = {"Styczeń": 1, "Luty": 2, "Marzec": 3, "Kwiecień": 4, "Maj": 5, "Czerwiec": 6, "Lipiec": 7, "Sierpień": 8, "Wrzesień": 9, "Październik": 10, "Listopad": 11, "Grudzień": 12}
    current_calendar = driver.find_element(by=By.XPATH, value="//div[@class='wHSr-monthName']")
    current_calendar = current_calendar.text
    current_calendar = current_calendar.split(' ')[0]
    current_month = calendar_dict[current_calendar]
    given_month = dep_date.month

    if (given_month<current_month):
        left = driver.find_element(by=By.XPATH, value="//button[@aria-label='Poprzedni miesiąc']")
        while (given_month<current_month):
            left.click()
            time.sleep(random.uniform(0.2, 1))
            current_month-=1

    if (given_month>current_month):
        right = driver.find_element(by=By.XPATH, value="//button[@aria-label='Następny miesiąc']")
        while (given_month>current_month):
            right.click()
            time.sleep(random.uniform(0.2, 1))
            current_month+=1    
    
    dep_date = process_date(dep_date)
    
    path = "//div[@aria-label='" + dep_date + "']"
    date_button = driver.find_element(
        by=By.XPATH, value=path
    )
    date_button.click()

def ret_date_chooser(ret_date, driver):


    ret_date = process_date(ret_date)
    path = "//div[@aria-label='" + ret_date + "']"
    date_button = driver.find_element(
        by=By.XPATH, value=path)
    date_button.click()

def tickets(driver, adults, students, teenagers, children):
    ticket = driver.find_element(by=By.XPATH, value="//div[@role='button' and contains(@class, 'S9tW')]")
    ticket.click()
    time.sleep(5)

    if (students == 9):
        plus = driver.find_elements(by=By.XPATH, value="//button[@aria-label='Mniej' and @aria-disabled='false']")
        plus[1].click()
        time.sleep(random.uniform(0.2, 1))
        minus = driver.find_element(by=By.XPATH, value="//button[@aria-label='Mniej' and @aria-disabled='false']")
        minus.click()
        
        s = 1
        while (s<students):
            plus[1].click()
            s+=1
        
    else:
        plus = driver.find_elements(by=By.XPATH, value="//button[@aria-label='Mniej' and @aria-disabled='false']")
        a = 1
        while (a<adults):
            plus[0].click()
            time.sleep(random.uniform(0.2, 1))
            a+=1

        s = 0
        while (s<students):
            plus[1].click()
            time.sleep(random.uniform(0.2, 1))
            s+=1
        
        if (adults==0):
            minus = driver.find_elements(by=By.XPATH, value="//button[@aria-label='Mniej' and @aria-disabled='true']")
            minus[2].click()

    t = 0
    while (t<teenagers):
        plus[2].click()
        time.sleep(random.uniform(0.2, 1))
        t+=1

    c = 0
    while (c<children):
        plus[3].click()
        time.sleep(random.uniform(0.2, 1))
        c+=1



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

def get_flight_data_multi(index, index4, index8, df, driver):

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

    # price per person
    price = driver.find_elements(by=By.XPATH, value="//span[@class='price-text']")
    l.append(price[index].text)

    #prize total
    price_total = driver.find_elements(by=By.XPATH, value="//div[@class='price-total']")
    l.append(price_total[index].text)

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

    time.sleep(1)
    df.to_excel(file_name, sheet_name="sheet1")


def process_results_multi(driver, file_name):

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
        "prize_per_person",
        "prize_total"
    )
    df = pd.DataFrame(columns=columns)
    
    cheapest_results(driver)
    time.sleep(5)
    index = 0
    index4 = 0
    index8 = 0

    while index < 15:
        get_flight_data_multi(index, index4, index8, df, driver)
        index += 1
        index4 += 4
        index8 += 8
    load_more(driver)
    time.sleep(5)

    while index < 30:
        get_flight_data_multi(index, index4, index8, df, driver)
        index += 1
        index4 += 4
        index8 += 8

    time.sleep(1)
    df.to_excel(file_name, sheet_name="sheet1")

def process_date(date):
    dict_month = {1: "sty", 2: "lut", 3: "mar", 4: "kwi", 5: "Maj", 6: "cze", 7: "lip", 8: "sie", 9: "wrz", 10: "paź", 11: "lis", 12: "gru"}
    return str('{:02d}'.format(date.day)) + " " + dict_month[date.month] + " " + str(date.year)

def proceed_search(driver, dep_country, ret_country, dep_date, ret_date, email, adults, students, teenagers, children):
    closeCookie(driver)
    time.sleep(random.uniform(0.5, 2))
    dep_country_chooser(dep_country, driver)
    time.sleep(random.uniform(0.5, 2))
    ret_country_chooser(ret_country, driver)
    time.sleep(random.uniform(0.5, 2))
    dep_date_chooser(dep_date, driver)
    time.sleep(random.uniform(0.5, 2))
    ret_date_chooser(ret_date, driver)
    time.sleep(random.uniform(0.5, 2))
    tickets(driver, adults, students, teenagers, children)
    time.sleep(random.uniform(0.5, 2))
    submit_search(driver)
    time.sleep(30)
    file_name = dep_country + "_" + ret_country + "_" + dep_date.strftime("%y-%m-%d") + "_" + ret_date.strftime("%y-%m-%d")
    actual_time = datetime.now().strftime("%Y.%m.%d %H:%M")
    file_name = file_name + " " + actual_time + ".xlsx"
    if (adults+students==1):
        process_results(driver, file_name)
    else:
        process_results_multi(driver, file_name)
    
    email_send.sender("Wynik wyszukiwania: " + actual_time, file_name, email)
    driver.quit()



def search_button(dep_country, ret_country, dep_date, ret_date, email, cooldown, amount, adults, students, teenagers, children):
    dict_cooldown = {"12 godzin": 43200, "24 godziny": 86400, "48 godzin": 172800, "1 minuta": 60}
    cooldown = dict_cooldown[cooldown]
    j = 0
    while (j<amount):
        i = 0
        b = True
        while(i<5 and b):
            try:
                link = "https://www.kayak.pl/flights"
                driver = webdriver.Chrome(executable_path="D:\Program Files (x86)\chromedriver\chromedriver.exe")
                driver.maximize_window()
                driver.get(link)
                time.sleep(10)        
                proceed_search(driver, dep_country, ret_country, dep_date, ret_date, email, adults, students, teenagers, children)
                b=False
                
            except Exception as e: 
                driver.quit()
                print(e)
            i+=1
        if(amount>1):
            time.sleep(cooldown)
        j+=1
