import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestCheckChapterBread:
    def test_check_chapter_bread(self, start_from_login_page):
        driver = start_from_login_page

        # Нажали на раздел начинки "Соусы"
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.inscription_sauсe)).click()

        # Нажали на раздел "Булки"
        WebDriverWait(driver,10).until(
            EC.visibility_of_element_located(Locators.inscription_bread)).click()

        # Проверяем наличие активного раздела
        active_element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located(Locators.active_section))
        assert active_element.is_displayed()

        # Проверяем, что активная вкладка соответствует разделу "Булки"
        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.active_section))
        assert "Булки" in active_tab.text


class TestCheckChapterFillings:
    def test_check_chapter_fillings(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        # Нажали на раздел "Начинки"
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.inscription_fillings)).click()

        # Проверяем наличие активного раздела
        active_element = WebDriverWait(driver,10).until(
            EC.presence_of_element_located(Locators.active_section))
        assert active_element.is_displayed()

        # Проверяем, что активная вкладка соответствует разделу "Начинки"
        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.active_section))
        assert "Начинки" in active_tab.text


class TestCheckChapterSauce:
    def test_check_chapter_sauce(self, start_from_login_page):
        driver = start_from_login_page
        driver.maximize_window()

        # Нажали на раздел "Соусы"
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.inscription_sauсe)).click()

        # Проверяем наличие активного раздела
        active_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(Locators.active_section))
        assert active_element.is_displayed()

        # Проверяем, что активная вкладка соответствует разделу "Соусы"
        active_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.active_section))
        assert "Соусы" in active_tab.text