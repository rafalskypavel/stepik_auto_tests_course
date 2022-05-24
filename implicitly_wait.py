from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/wait1.html")
button = browser.find_element(By.ID, "verify")

button.click()

message = browser.find_element(By.ID, "verify_message")


assert "successful" in message.text


# Если произойдет ошибка, то WebDriver выбросит одно из следующих исключений (exceptions):
#
#     Если элемент не был найден за отведенное время, то мы получим NoSuchElementException.

#     Если элемент был найден в момент поиска, но при последующем обращении к элементу DOM изменился,
#     то получим StaleElementReferenceException. Например, мы нашли элемент Кнопка и через какое-то
#     время решили выполнить с ним уже известный нам метод click. Если кнопка за это время была скрыта
#     скриптом, то метод применять уже бесполезно — элемент "устарел" (stale) и мы увидим исключение.

#     Если элемент был найден в момент поиска, но сам элемент невидим (например, имеет нулевые размеры),
#     и реальный пользователь не смог бы с ним взаимодействовать, то получим ElementNotVisibleException.
