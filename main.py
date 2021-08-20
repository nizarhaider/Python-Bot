import random
from selenium import webdriver
import pandas as pd

df = pd.read_excel("Email list.xlsx")

mails = df['Emails']
mails = mails.to_list()

names = df['Names']
names = names.to_list()

Organization = df['Organization']
Org = Organization.to_list()

b = random.randint(0, 14)

Why = df['Why did i choose this team']
Why = Why.to_list()
Imp = df['Improvement']
Imp = Imp.to_list()
a = random.randint(0, 14)

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
# option.add_experimental_option("excludeSwitches", ['enable-automation']);
# option.add_argument("--headless")
# option.add_argument("disable-gpu")

browser = webdriver.Chrome(executable_path="C:/Users/hagid/Desktop/chromedriver_win32/chromedriver.exe",
                           options=option)

for num in range(140,147):
    browser.maximize_window()

    browser.get("https://airtable.com/shrm8YSMqxKcNLb8a")

    textboxes = browser.find_element_by_class_name("fit")
    textboxes.click()
    teams = browser.find_elements_by_class_name("col-12")
    teams[0].send_keys("Portasonic")
    browser.implicitly_wait(100)

    option = browser.find_element_by_class_name("rowSuggestion")
    option.click()

    Name = browser.find_elements_by_class_name("col-12")
    Name[2].send_keys(str(names[num]))

    Email = browser.find_elements_by_class_name("col-12")
    Email[3].send_keys(str(mails[num]))

    Organization = browser.find_elements_by_class_name("col-12")
    Organization[4].send_keys("UTM")

    Reason = browser.find_elements_by_class_name("contentEditableTextbox")
    Reason[0].send_keys(Why[b])

    Improvement = browser.find_elements_by_class_name("contentEditableTextbox")
    Improvement[1].send_keys(str(Imp[a]))

    # tickbox = browser.find_elements_by_class_name("flex-none")
    # tickbox[3].click()

    submitbutton = browser.find_element_by_class_name("submitButton")
    submitbutton.click()

    browser.implicitly_wait(100)

    back = browser.find_element_by_class_name("mr2")
    back.click()
