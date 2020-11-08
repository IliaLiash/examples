from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
 
try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
        
    element1 = browser.find_element_by_css_selector("#num1")
    x = element1.text
    element2 = browser.find_element_by_css_selector("#num2")
    y = element2.text
    
    res = int(x) + int(y)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(res))
        
    #нажимаем кнопку отправки формы
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()