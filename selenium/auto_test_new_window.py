from selenium import webdriver
import math
import time
import os
'''
Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
'''    
def calc(x):
    return str(math.log(abs(12*math.sin(int(x))))) 
 
try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
     
    #нажимаем кнопку
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()    
    
    #переключаемся на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)    
        
    #решаем капчу
    element = browser.find_element_by_css_selector("#input_value")
    x = element.text
    y = calc(x)
    
    #вводим данные в поле и нажимаем кнопку
    input1 = browser.find_element_by_css_selector(".form-control")
    input1.send_keys(y)
    button1 = browser.find_element_by_css_selector(".btn.btn-primary")
    button1.click()        
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()