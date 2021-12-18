import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test(self):
        # ТЕСТ РЕГИСТРАЦИИ НЕ УДАЛОСЬ
        s = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=s)
        browser.get('http://127.0.0.1:8000/reg')
        el_name = browser.find_element_by_name("username")
        el_name.send_keys("gffctftfffcfct")
        el_name = browser.find_element_by_name("first_name")
        el_name.send_keys("gffctftfffcfct")
        el_name = browser.find_element_by_name("last_name")
        el_name.send_keys("gffctftfffcfct")
        el_name = browser.find_element_by_name("email")
        el_name.send_keys("gffctftfffcfct@mail.ru")
        el_name = browser.find_element_by_name("password1")
        el_name.send_keys("gffctftfffcfct")
        el_name = browser.find_element_by_name("password2")
        el_name.send_keys("gffctftfffcfct")
        browser.find_element_by_id("main_button").click()
        error_mes = browser.find_element_by_id("error")
        assert error_mes.text == "Не удалось зарегистрировать пользователя"
        time.sleep(5)


    def test_reg_success(self):
        # ТЕСТ РЕГИСТРАЦИИ УСПЕШНО
        # button = driver.find_element(By.CLASS_NAME, "quiz_button")
        # element = find_element_by_id("main_button")
        s = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=s)
        browser.get('http://127.0.0.1:8000/reg')
        el_name = browser.find_element_by_name("username")
        el_name.send_keys("pozdyshevdan")
        el_name = browser.find_element_by_name("first_name")
        el_name.send_keys("daniil")
        el_name = browser.find_element_by_name("last_name")
        el_name.send_keys("pozdyshev")
        el_name = browser.find_element_by_name("email")
        el_name.send_keys("pozdyshevdan@yandex.ru")
        el_name = browser.find_element_by_name("password1")
        el_name.send_keys("Rq`H-!c#g2'k'JFx")
        el_name = browser.find_element_by_name("password2")
        el_name.send_keys("Rq`H-!c#g2'k'JFx")
        browser.find_element_by_id("main_button").click()
        mes = browser.find_element_by_id("error")
        assert mes.text == "Успешно зарегестрирован"
        time.sleep(5)


    def test_auth_failed(self):
        # ТЕСТ АВТОРИЗАЦИИ ПРОВАЛЬНЫЙ пароль
        # button = driver.find_element(By.CLASS_NAME, "quiz_button")
        # element = find_element_by_id("main_button")
        s = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=s)
        browser.get('http://127.0.0.1:8000/auth')
        el_name = browser.find_element_by_name("email")
        el_name.send_keys("pozdyshevdan@yandex.ru")
        el_name = browser.find_element_by_name("password")
        el_name.send_keys("Rq`H-!c#g2'k'JF0")
        browser.find_element_by_id("main_button").click()
        password_falird = browser.find_element_by_class_name("error")
        assert password_falird.text == "Неверный пароль"
        time.sleep(50000)


    def test_auth_email_failed(self):
        # ТЕСТ АВТОРИЗАЦИИ ПРОВАЛЬНАЯ почта
        # button = driver.find_element(By.CLASS_NAME, "quiz_button")
        # element = find_element_by_id("main_button")
        s = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=s)
        browser.get('http://127.0.0.1:8000/auth')
        el_name = browser.find_element_by_name("email")
        el_name.send_keys("pozdyshevdan@mail.ru")
        el_name = browser.find_element_by_name("password")
        el_name.send_keys("Rq`H-!c#g2'k'JF0")
        browser.find_element_by_id("main_button").click()
        password_falird = browser.find_element_by_class_name("error")
        assert password_falird.text == "Неверная почта"
        time.sleep(5)


    def test_auth_succeed(self):
        # ТЕСТ АВТОРИЗАЦИИ УСПЕШНО
        # button = driver.find_element(By.CLASS_NAME, "quiz_button")
        # element = find_element_by_id("main_button")
        s = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=s)
        browser.get('http://127.0.0.1:8000/auth')
        el_name = browser.find_element_by_name("email")
        el_name.send_keys("pozdyshevdan@yandex.ru")
        el_name = browser.find_element_by_name("password")
        el_name.send_keys("Rq`H-!c#g2'k'JFx")
        browser.find_element_by_id("main_button").click()
        email = browser.find_element_by_class_name("profile_info__mail")
        assert email.text == "pozdyshevdan@yandex.ru"
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()