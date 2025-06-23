
from selenium.webdriver.common.by import By
from data import Credential

class Locators:
    # Кнопка "Войти в аккаунт" на главной странице
    entrance_on_the_main = (By.XPATH,  "//button[contains(text(), 'Войти в аккаунт')]")

    # Основное лого
    logo = (By.XPATH, '//header/nav/div')

    # Надпись "выход"
    button_exit = (By.XPATH, ".//button[contains(text(), 'Выход')]")

    # Надписи "профиль"
    inscription_profile = (By.XPATH, './/a[@href="/account/profile"]')

    # Надписи "булки"
    inscription_bread = (By.XPATH, ".//span[contains(text(), 'Булки')]")

    # Кнопка "личный кабинет"
    button_personal_area = (By.XPATH, ".//p[contains(text(), 'Личный Кабинет')]")

    # Надпись "Соусы"
    inscription_sauсe = (By.XPATH, "//span[contains(text(), 'Соусы')]")

    # Надпись "Зарегистрироваться"
    inscription_login = (By.CLASS_NAME, "Auth_link__1fOlj")

    # Раздел "Начинки"
    inscription_fillings = (By.XPATH, "//span[contains(text(), 'Начинки')]")

    # Активный раздел
    active_section = (By.XPATH, '//div[contains(@class, "tab_tab_type_current")]')

    # Надпись "Такой пользователь уже существует"
    inscription_error_account = (By.XPATH, "//p[contains(text(), 'Такой пользователь уже существует')]")

    # Надпись "Некорректный пароль"
    inscription_error_password = (By.XPATH, '//div[contains(@class, "input_status_error")]')

    # Кнопка "восстановить пароль"
    button_restore_password = (By.XPATH, "//a[contains(@href, 'forgot-password')]")

    # Кнопка "войти"
    inscription_button_entrance = (By.XPATH, '//a[@href="/login"]')

    # Кнопка "Войти"
    button_entrance = (By.XPATH, "//button[contains(text(), 'Войти')]")

    # Кнопка "Оформить заказ"
    button_arrange_order = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")

    # Кнопка "Зарегистрироваться"
    button_login = (By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]")

    # Кнопка "Конструктор"
    button_constraction = (By.XPATH, "//a[@href='/']")

    # Поле "Имя"
    field_name = (By.XPATH, "//div[label[contains(text(), 'Имя')]]//input")

    # Поле "email"
    field_email = (By.XPATH, "//div[label[contains(text(), 'Email')]]//input")

    # Поле "password"
    field_password = (By.XPATH, "//div[label[contains(text(), 'Пароль')]]//input")
