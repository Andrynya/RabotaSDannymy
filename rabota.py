import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://www.divan.ru/category/svet"

driver.get(url)

time.sleep(5)

lampy = driver.find_elements(By.CLASS_NAME, 'lsooF')

parsed_data = []

for lampa in lampy:
    try:
        name = lampa.find_element(By.CSS_SELECTOR, "span[itemprop='name']").text
        price = lampa.find_element(By.CSS_SELECTOR, 'meta[itemprop="price"]').text
        link = lampa.find_element(By.CSS_SELECTOR, 'link[itemprop="url"]').get_attribute('href')
    except:
        print(f"Произошла ошибка")
        continue

    parsed_data.append([name, price, link])

driver.quit()

with open("svet.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'Ссылка'])
    writer.writerows(parsed_data)