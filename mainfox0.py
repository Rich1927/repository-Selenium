from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import WebDriverException
import time
import sys
import os

# Путь к geckodriver, если он не в системном PATH (можно указать явно)
# Пример: service = Service(executable_path="C:/Drivers/geckodriver.exe")
service = Service()  # если geckodriver уже в PATH

try:
    print("🔄 Запуск браузера Firefox...")
    browser = webdriver.Firefox(service=service)

    print("🌐 Переход на страницу Википедии...")
    browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
    browser.save_screenshot("dom.png")#Доб. автоматизированный скриншотинг:

    print("⏳ Ожидание 5 или 10 секунд...")
    time.sleep(5)
    browser.save_screenshot("selenium.png")

    print("✅ Закрытие браузера.")
    browser.quit()
    print("🏁 Программа завершена успешно.")

except WebDriverException as e:
    print("❌ Произошла ошибка при запуске браузера или переходе по ссылке.")
    print("Описание ошибки:", e)
    print("Проверь, установлен ли geckodriver и добавлен ли он в системный PATH.")
    sys.exit(1)

except Exception as e:
    print("❌ Возникла неожиданная ошибка.")
    print("Описание ошибки:", e)
    sys.exit(1)
