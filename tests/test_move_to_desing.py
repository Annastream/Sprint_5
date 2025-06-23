import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

@pytest.mark.parametrize("section_data", [
    {
        "name": "Булки",
        "click_locator": Locators.inscription_bread,
        "pre_click_locator": Locators.inscription_sauсe
    },
    {
        "name": "Начинки",
        "click_locator": Locators.inscription_fillings,
        "pre_click_locator": None
    },
    {
        "name": "Соусы",
        "click_locator": Locators.inscription_sauсe,
        "pre_click_locator": None
    }
])
class TestMenuSections:
    def test_section_activation(self, start_from_login_page, section_data):
        driver = start_from_login_page
        driver.maximize_window()

        # Дополнительный клик для теста булок (чтобы проверить переключение)
        if section_data["pre_click_locator"]:
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located(section_data["pre_click_locator"])).click()

        # Клик по целевому разделу
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(section_data["click_locator"])).click()

        # Проверка активного раздела
        active_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(Locators.active_section))
        assert active_element.is_displayed()

        # Проверка соответствия текста
        active_tab = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located(Locators.active_section))
        assert section_data["name"] in active_tab.text