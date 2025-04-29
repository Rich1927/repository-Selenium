from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Запуск браузера Firefox
browser = webdriver.Firefox()

def open_article(query):
    url_query = query.replace(" ", "_")
    url = f"https://ru.wikipedia.org/wiki/{url_query}"
    browser.get(url)
    time.sleep(1)

def list_paragraphs():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    print("\n📄 Параграфы статьи. Нажмите Enter для следующего, 'stop' — для остановки.\n")
    for paragraph in paragraphs:
        text = paragraph.text.strip()
        if text:
            print(text, "\n")
            try:
                user_input = input("▶ Продолжить? (Enter / stop): ").strip().lower()
                if user_input == "stop":
                    break
            except:
                break

def choose_internal_link():
    links = browser.find_elements(By.CSS_SELECTOR, "div.mw-parser-output a")
    internal_links = [a for a in links if a.get_attribute("href") and "/wiki/" in a.get_attribute("href") and ":" not in a.get_attribute("href")]

    if not internal_links:
        print("❌ Внутренние ссылки не найдены.")
        return None

    # Показываем первые 5 уникальных ссылок
    seen = set()
    options = []
    for a in internal_links:
        title = a.text.strip()
        href = a.get_attribute("href")
        if title and title not in seen:
            seen.add(title)
            options.append((title, href))
        if len(options) == 5:
            break

    print("\n🔗 Внутренние статьи:")
    for i, (title, _) in enumerate(options, start=1):
        print(f"{i}. {title}")

    choice = input("Введите номер статьи для перехода (или Enter для отмены): ").strip()
    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(options):
            browser.get(options[index][1])
            time.sleep(1)
            return True
    print("❌ Неверный выбор или отмена.")
    return False

# Основной цикл
try:
    while True:
        query = input("\n🔍 Что ищем на Википедии? (или 'exit' для выхода): ").strip()
        if query.lower() == "exit":
            break

        open_article(query)

        while True:
            print("\n📋 Действия:")
            print("1 — Читать параграфы")
            print("2 — Перейти на внутреннюю статью")
            print("3 — Новый поиск")
            print("4 — Выход")
            action = input("Выберите: ").strip()

            if action == "1":
                list_paragraphs()
            elif action == "2":
                choose_internal_link()
            elif action == "3":
                break
            elif action == "4":
                raise SystemExit
            else:
                print("⚠️ Неверный ввод.")
finally:
    browser.quit()
