# 3.Необходимо спарсить цены на диваны с сайта divan.ru в csv файл, обработать данные,
# найти среднюю цену и вывести ее, а также сделать гистограмму цен на диваны
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
import time

# Импортируем модуль CSV
import csv

# Если используем Google Chrome, то пишем driver = webdriver.Chrome()
driver = webdriver.Chrome()
# driver = webdriver.Firefox()

# URL страницы\
url = 'https://www.divan.ru/ekaterinburg/category/divany-i-kresla'

# Открытие страницы
driver.get(url)

# Ждем некоторое время, чтобы страница полностью загрузилась
time.sleep(5)

# <span class="ui-LD-ZU KIkOH" data-testid="price">68 240<span class="ui-i5wwi ui-VDyJR ui-VWOa-">руб.</span></span>

# Парсинг цен
prices = driver.find_elements(By.CSS_SELECTOR, "span.ui-LD-ZU")  # = "span.ui-LD-ZU.KIkOH"

# Открытие CSV файла для записи
with open('prices_divan.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])  # Записываем заголовок столбца

    # Записываем цены в CSV файл
    for price in prices:
        writer.writerow([price.text])

# Закрытие драйвера
driver.quit()
