from selenium import webdriver
import math
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
'''
Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Book"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
'''    
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))     

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    #ищем кнопку, задаем параметыр ожидания
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")    
       )
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()
    
    #решаем капчу
    element = browser.find_element_by_css_selector("#input_value")
    x = element.text
    y = calc(x)
    
    #вводим данные в поле и нажимаем кнопку
    browser.execute_script("window.scrollBy(0, 100);")    
    input1 = browser.find_element_by_css_selector(".form-control")
    input1.send_keys(y)
    
    button1 = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.ID, "solve"))   
       )    
    
    button1.click()        
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()