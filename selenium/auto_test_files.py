from selenium import webdriver
import math
import time
import os
'''
Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Submit"
'''    
 
try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
        
    input1 = browser.find_element_by_name('firstname')
    input1.send_keys("Sergey")
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("Brin")
    input3 = browser.find_element_by_name('email')
    input3.send_keys("zdarova@otets")
    
    element = browser.find_element_by_css_selector("#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    element.send_keys(file_path)        
        
    #нажимаем кнопку отправки формы
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()