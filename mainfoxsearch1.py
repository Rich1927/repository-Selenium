from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import WebDriverException
import time
import sys

def choose_browser():
    choice = input("Выберите браузер (firefox/chrome): ").strip().lower()
    if choice == "firefox":
        return webdriver.Firefox(service=FirefoxService())
    elif choice == "chrome":
        return webdriver.Chrome(service=ChromeService())
    else:
        print("❌ Неподдерживаемый браузер. Используйте 'firefox' или 'chrome'.")
        sys.exit(1)

try:
    browser = choose_browser()

    print("🌐 Переход на главную страницу Википедии...")
    browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

    # Проверка заголовка
    assert "Википедия" in browser.title
    print("✅ Заголовок страницы подтверждён.")

    time.sleep(2)

    print("🔍 Поиск поля ввода...")
    search_box = browser.find_element(By.ID, "searchInput")

    print("⌨️ Ввод поискового запроса...")
    search_box.send_keys("Солнечная система")
    search_box.send_keys(Keys.RETURN)

    print("⏳ Ожидание загрузки результатов...")
    time.sleep(5)

    print("📸 Сохранение скриншота результатов поиска...")
    browser.save_screenshot("search_result.png")
    print("✅ Скриншот сохранён как search_result.png")

    print("🚪 Закрытие браузера.")
    browser.quit()

except WebDriverException as e:
    print("❌ Ошибка при работе с веб-драйвером.")
    print("Описание:", e)
    sys.exit(1)

except Exception as e:
    print("❌ Неожиданная ошибка.")
    print("Описание:", e)
    sys.exit(1)
