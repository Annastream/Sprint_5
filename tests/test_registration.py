from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from geniration_ep import EmailPasswordGenerator
from locators import Locators
from curl import *
from data import Credential
from tests.conftest import register_new_account, start_from_main_not_login


@pytest.mark.usefixture("register_new_account")
class TestCheckNewRegister:
    def test_registration(self, register_new_account):
        driver, email, password = register_new_account


        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.field_password).send_keys(password)
        driver.find_element(*Locators.button_entrance).click()
        WebDriverWait(driver, 30).until(EC.url_to_be(main_site))
        assert driver.current_url == main_site


@pytest.mark.usefixtures("start_from_main_not_login")
class TestCheckingCreationExistingAccount:
    def test_existing_account(self, start_from_main_not_login):
        driver = start_from_main_not_login

        driver.find_element(*Locators.inscription_login).click()
        # Найди поле "Имя" и заполни его
        driver.find_element(*Locators.field_name).send_keys(Credential.name)
        # Найди поле "email" и заполни его
        driver.find_element(*Locators.field_email).send_keys(Credential.email)
        # Найди поле "Пароль" и заполни его
        driver.find_element(*Locators.field_password).send_keys(Credential.password)
          # Жмем на зарегаться
        driver.find_element(*Locators.button_login).click()
             # ждем ошибку регистрации

        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_error_account))

def test_enter_button_personal_area(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")



    driver.find_element(*Locators.button_personal_area).click()

    WebDriverWait(driver, 20).until(EC.url_to_be(login_site))

    driver.find_element(*Locators.field_email).send_keys(Credential.email)
    driver.find_element(*Locators.field_password).send_keys(Credential.password)
    driver.find_element(*Locators.button_entrance).click()
    WebDriverWait(driver, 30).until(EC.url_to_be(main_site))
    assert driver.current_url == main_site


@pytest.mark.usefixture("start_from_main_not_login")
class TestCheckRegisterNoName:
    def test_registration_no_name(self, start_from_main_not_login):
        driver = start_from_main_not_login

        driver.find_element(*Locators.inscription_login).click()

        # Генерация email и password
        generator = EmailPasswordGenerator()
        email, password = generator.generate()  # Вызываем метод generate() у объекта generator

        # Ищем поле "email" и заполни его
        driver.find_element(*Locators.field_email).send_keys(email)

        # Ищем поле "Пароль" и заполни его
        driver.find_element(*Locators.field_password).send_keys(password)

        # Нажать кнопку зарегистрироваться
        driver.find_element(*Locators.button_login).click()

        # Проверим, что мы на странице регистрации
        assert driver.current_url == register_site

@pytest.mark.usefixtures("start_from_main_not_login")
class TestCheckingErrorPassword:
    def test_error_password(self, start_from_main_not_login):
        driver = start_from_main_not_login
        driver.find_element(*Locators.inscription_login).click()
        driver.find_element(*Locators.field_name).send_keys(Credential.name)
        driver.find_element(*Locators.field_email).send_keys(Credential.email)
        driver.find_element(*Locators.field_password).send_keys(Credential.password)
        driver.find_element(*Locators.button_login).click()

        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.inscription_login))


    def test_no_password(self, start_from_main_not_login):
        driver = start_from_main_not_login
        email = 'igo@yandex.ru'
        driver.find_element (*Locators.inscription_login).click()
        # Найди поле "Имя" и заполни его
        driver.find_element(*Locators.field_name).send_keys(Credential.name)
        # Найди поле "email" и заполни его
        driver.find_element(*Locators.field_email).send_keys(email)
        # Жмем на зарегистрироваться
        driver.find_element(*Locators.button_login).click()
        # Проверка текущего URL, должны остаться на странице регистрации
        assert driver.current_url == register_site


class TestCheckRegister:
    def test_login_password_recovery(self, start_from_recovery_page):
        driver = start_from_recovery_page

        # Ждем загрузки "булок"
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(Locators.inscription_bread))

        # Проверяем что мы на основной странице сайта
        assert driver.current_url == main_site


class TestCheckEntranceFromRecoveryPage:
    def test_button_inscription_login(self, start_from_main_not_login):
        driver = start_from_main_not_login

        # Жмем кнопку "Войти"
        driver.find_element(*Locators.inscription_login).click()

        # Жмем кнопку "войти" на форме входа
        driver.find_element(*Locators.inscription_button_entrance).click()

        # Ищем поля и проходим авторизацию
        driver.find_element(*Locators.field_email).send_keys(Credential.email)
        driver.find_element(*Locators.field_password).send_keys(Credential.password)
        driver.find_element(*Locators.button_entrance).click()

        # Ждем перехода на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        # Проверяем что мы на основной странице сайта
        assert driver.current_url == main_site





