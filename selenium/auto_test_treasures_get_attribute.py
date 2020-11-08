from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))    
 
try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
        
    element = browser.find_element_by_css_selector("#treasure")
    x = element.get_attribute("valuex")    
    
    y = calc(x)
    
    #ищем форму, чтобы отправить в нее y
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)  
    #ставим галочки, точечки в checkbox и radiobox
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()        
    #нажимаем кнопку отправки формы
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()