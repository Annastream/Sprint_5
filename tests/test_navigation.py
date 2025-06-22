import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from curl import *


class TestTransitionByConstructor:
    def test_check_transition_by_constructor(self, start_from_main_page):
        driver = start_from_main_page


        # Ждем перехода на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        # Кликаем по кнопке "личный кабинет"
        driver.find_element(*Locators.button_personal_area).click()

        # Ждем загрузки надписи "конструктор"
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.button_constraction))

        # Кликаем по кнопке "конструктор"
        driver.find_element(*Locators.button_constraction).click()

        # Ждем перехода на главную страницу
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        # Проверяем что мы на основной странице
        assert driver.current_url == main_site


class TestTransitionByLogo:
    def test_transition_by_logo(self, start_from_login_page):
        driver = start_from_login_page


        # Ждем загрузки надписи "профиль"
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.button_personal_area))

        # Кликаем по кнопке "личный кабинет"
        driver.find_element(*Locators.button_personal_area).click()

        # Ждем загрузки надписи "профиль"
        WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located(Locators.inscription_profile))

        # Кликаем по "logo"
        driver.find_element(*Locators.logo).click()

        # Ждем перехода на главную страницу

        WebDriverWait(driver,10).until(EC.url_to_be(main_site))

        # Проверяем, что мы на основной странице
        assert driver.current_url == main_site

        # Переход на главную страницу через логотип не выполнен


class TestCheckPageProfile:
    def test_transition_before_profile(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        # Ждем загрузки "булок"
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.inscription_bread))

        # Кликаем по кнопке "личный кабинет"
        driver.find_element(*Locators.button_personal_area).click()

        # Ждем перехода на страницу профиля
        WebDriverWait(driver, 10).until(
            EC.url_to_be(profile_site))

        # Проверяем что мы на странице профиля
        assert driver.current_url == profile_site