from selenium import webdriver
import time
#С помощью time мы можем делать задержки в программе
#Если мы работаем с Firefox
browser = webdriver.Firefox()
#Настраиваем возможность зайти на сайт.
browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
#В кавычках указываем URL сайта, на который нам нужно зайти
time.sleep(10)
#Задержка в 10 секунд
browser.quit()
#Закрываем браузер