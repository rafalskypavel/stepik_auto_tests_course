from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной

    button = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button2 = browser.find_element(By.ID, "book").click()


    readen_X = browser.find_element(By.XPATH, '//span[@id="input_value"]')
    x = readen_X.text
    y = calc(int(x))

    input_answer = browser.find_element(By.ID, 'answer').send_keys(y)
    option3 = browser.find_element(By.ID, "solve").click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()


# Если мы захотим проверять, что кнопка становится неактивной после отправки данных,
# то можно задать негативное правило с помощью метода until_not:

# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
# button = WebDriverWait(browser, 5).until_not(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )



# assert "successful" in message.text
#
