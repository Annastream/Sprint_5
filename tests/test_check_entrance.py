from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from curl import *
from data import Credential

class TestButtonCheckExit:

    def test_check_login_out(self, start_from_login_page):
        driver = start_from_login_page    # вход/выход в/из учетной записи пользователя

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_bread))

        driver.find_element(*Locators.button_personal_area).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_profile))

        driver.find_element(*Locators.button_exit).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(login_site))

        assert driver.current_url == login_site

class TestBigMainButton:
    def test_check_entrance_by_big_button(self, start_from_site_not_login):
        driver = start_from_site_not_login # входа в систему через главную страницу сайта

        driver.find_element(*Locators.entrance_on_the_main).click()

        # войди в аккаунт
        driver.find_element(*Locators.field_email).send_keys(Credential.email)
        driver.find_element(*Locators.field_password).send_keys(Credential.password)
        driver.find_element(*Locators.button_entrance).click()

        # Ожидание перехода на главную страницу
        WebDriverWait(driver,15).until(EC.url_to_be(main_site))

        # Проверка, мы на основной странице сайта
        assert driver.current_url == main_site

        class TestCheckRegister:
            def test_login_password_recovery(self, start_from_recovery_page):
                driver = start_from_recovery_page

                WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.inscription_bread))
                assert driver.current_url == main_site





