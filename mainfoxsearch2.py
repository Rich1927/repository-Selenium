from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import random

# 1. Запускаем Firefox и открываем статью "Солнечная система"
browser = webdriver.Firefox()
browser.get("https://ru.wikipedia.org/wiki/Солнечная_система")

# 2–4. Печатаем каждый параграф статьи по Enter, с защитой от ошибок ввода
print("🔍 Печатаем параграфы по одному. Нажмите Enter для следующего (или закройте окно для выхода)...")
paragraphs = browser.find_elements(By.TAG_NAME, "p")
for paragraph in paragraphs:
    print(paragraph.text)
    try:
        input("▶ Нажмите Enter для продолжения...")
    except (EOFError, UnicodeDecodeError):
        print("⚠️ Ввод недоступен или прерван. Прекращаем показ параграфов.")
        break

# 5. Находим div'ы с классом "hatnote navigation-not-searchable"
hatnotes = []
for element in browser.find_elements(By.TAG_NAME, "div"):
    cl = element.get_attribute("class")
    if cl == "hatnote navigation-not-searchable":
        hatnotes.append(element)

# Если нашлись такие элементы
if hatnotes:
    hatnote = random.choice(hatnotes)
    link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
    print(f"🔗 Переход по случайной ссылке: {link}")
    browser.get(link)
else:
    print("⚠️ Не найдено подходящих блоков с классом hatnote.")

# Дать время увидеть результат
time.sleep(10)
browser.quit()
