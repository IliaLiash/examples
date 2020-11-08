from selenium import webdriver
import math
import time
'''
Открыть страницу http://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "I'm the robot".
Переключить radiobutton "Robots rule!".
Нажать на кнопку "Submit".
''' 

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))     
 
try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
        
    element1 = browser.find_element_by_css_selector("#input_value")
    x = element1.text
    
    y = calc(x)
    
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(str(y))
    
    browser.execute_script("window.scrollBy(0, 200);")    
    
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()    
    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()        
    #нажимаем кнопку отправки формы
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()