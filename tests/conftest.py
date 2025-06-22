import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from curl import *
from locators import Locators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from geniration_ep import EmailPasswordGenerator
from data import Credential


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def start_from_login_page(driver):
    login_page = login_site
    driver.get(login_page)

    driver.find_element(*Locators.field_email).send_keys(Credential.email)
    driver.find_element(*Locators.field_password).send_keys(Credential.password)
    driver.find_element(*Locators.button_entrance).click()

    return driver

@pytest.fixture
def start_from_recovery_page(driver):
    login_page = login_site
    driver.get(login_page)

    driver.find_element(*Locators.button_restore_password).click()

    WebDriverWait(driver,10).until(EC.visibility_of_element_located(Locators.inscription_button_entrance))

    driver.find_element(*Locators.inscription_button_entrance).click()

    driver.find_element(*Locators.field_email).send_keys(Credential.email)
    driver.find_element(*Locators.field_password).send_keys(Credential.password)
    driver.find_element(*Locators.button_entrance).click()
    return driver

@pytest.fixture
def start_from_main_page(driver):
    main_page = main_site
    driver.get(main_page)

    driver.find_element(*Locators.button_personal_area).click()

    driver.find_element(*Locators.button_entrance).click()

    driver.find_element(*Locators.field_email).send_keys(Credential.email)
    driver.find_element(*Locators.field_password).send_keys(Credential.password)
    driver.find_element(*Locators.button_entrance).click()
    return driver

@pytest.fixture
def start_from_register_page(driver):
    register_page = register_site
    driver.get(register_page)

    driver.find_element(*Locators.inscription_button_entrance).click()

    driver.find_element(*Locators.field_email).send_keys(Credential.email)
    driver.find_element(*Locators.field_password).send_keys(Credential.password)
    driver.find_element(*Locators.button_entrance).click()

    return driver




@pytest.fixture
def start_from_main_not_login(driver):
   login_page = login_site
   driver.get(login_site)

   return driver

@pytest.fixture
def start_from_site_not_login(driver):
    login_page = main_site
    driver.get(login_page)

    return driver


@pytest.fixture
def register_new_account(driver):
    login_page = login_site
    driver.get(login_page)

    driver.find_element(*Locators.inscription_login).click()

    generator = EmailPasswordGenerator()
    email, password = generator.generate()
    driver.find_element(*Locators.field_name).send_keys(Credential.name)
    driver.find_element(*Locators.field_email).send_keys(email)
    driver.find_element(*Locators.field_password).send_keys(password)
    driver.find_element(*Locators.button_login).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.button_entrance))

    return driver, email, password

