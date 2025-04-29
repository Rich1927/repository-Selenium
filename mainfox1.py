from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import WebDriverException
import time
import sys

# Убедись, что geckodriver в PATH или укажи путь вручную:
# service = Service(executable_path="C:/path/to/geckodriver.exe")
service = Service()

try:
    print("🔄 Запуск браузера Firefox...")
    browser = webdriver.Firefox(service=service)

    print("🌐 Переход на страницу Википедии...")
    browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")

    print("📸 Сохранение первого скриншота...")
    browser.save_screenshot("dom.png")

    print("⏳ Ожидание 5 секунд перед обновлением страницы...")
    time.sleep(5)

    print("🔁 Перезагрузка страницы...")
    browser.refresh()

    print("📸 Сохранение второго скриншота...")
    time.sleep(3)  # Подождём, пока страница обновится
    browser.save_screenshot("selenium.png")

    print("✅ Закрытие браузера...")
    browser.quit()
    print("🏁 Программа завершена успешно.")

except WebDriverException as e:
    print("❌ Ошибка при работе с браузером или загрузке страницы.")
    print("Описание:", e)
    sys.exit(1)

except Exception as e:
    print("❌ Неожиданная ошибка.")
    print("Описание:", e)
    sys.exit(1)
