import pytest
driver = webdriver.Chrome("\chromedriver.exe")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('./chromedriver.exe')
    # Переходим на страницу авторизации
    pytest.driver.get(
        'https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=f83be0e3-6a7d-4f24-add9-cc9887a4981c&theme&auth_type')

    driver.implicitly_wait(10)
    myDynamicElement = driver.find_element(By.ID, "kc-login")
    # Явные ожидания, кнопка Войти

    yield

    pytest.driver.quit()

# Позитивные тесты на проверку наличия на странице тех или иных элементов согласно документации:
# EXP-001

def test_show_tab_phone():
    tab_phone = pytest.driver.find_element(By.ID, 't-btn-tab-phone')
    if tab_phone is None:
        print("Таб выбора аутентификации по номеру не найден")
    else:
        print("Таб выбора аутентификации по номеру найден")

def test_show_tab_mail():
    tab_mail = pytest.driver.find_element(By.ID, 't-btn-tab-mail')
    if tab_mail is None:
        print("Таб выбора аутентификации по электронной почте не найден")
    else:
        print("Таб выбора аутентификации по электронной почте найден")

def test_show_tab_login():
    tab_login = pytest.driver.find_element(By.ID, 't-btn-tab-login')
    if tab_login is None:
        print("Таб выбора аутентификации по логину не найден")
    else:
        print("Таб выбора аутентификации по логину найден")

def test_show_tab_ls():
    tab_ls = pytest.driver.find_element(By.ID, 't-btn-tab-ls')
    if tab_ls is None:
        print("Таб выбора аутентификации по лицевому счету не найден")
    else:
        print("Таб выбора аутентификации по лицевому счету найден")

def test_show_input_username():
    input_username = pytest.driver.find_element(By.ID, 'username')
    if input_username is None:
        print("Форма ввода Номер или Логин или Почта или Лицевой счет не найдена")
    else:
        print("Форма ввода Номер или Логин или Почта или Лицевой счет найдена")

def test_show_input_password():
    input_password = pytest.driver.find_element(By.ID, 'password')
    if input_password is None:
        print("Форма ввода Пароль не найдена")
    else:
        print("Форма ввода Пароль найдена")

def test_show_forgot_password():
    forgot_password = pytest.driver.find_element(By.ID, 'forgot_password')
    if forgot_password is None:
        print("Кнопка Забыл пароль не найдена")
    else:
        print("Кнопка Забыл пароль найдена")

def test_show_authorization():
    input_username = pytest.driver.find_element(By.ID, 'kc-login')
    if input_username is None:
        print("Кнопка Войти не найдена")
    else:
        print("Кнопка Войти найдена")

def test_show_slogan():
    slogan = pytest.driver.find_element(By.XPATH,"//*[@id="page-left"]/div/div[2]/h2").text == "Ростелеком ID"
    if slogan is False:
        print("Слоган не соответствует документации")
    else:
        print("Слоган верный")

# Позитивный тест на авторизацию по номеру телефона
# EXP-002

def test_authorization_tab_phone():
    pytest.driver.find_element(By.ID, 't-btn-tab-phone').click()
    # Вводим phone
    pytest.driver.find_element(By.ID, 'username').send_keys('+79815045324')
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'password').send_keys('CevthrbVbhf-21586')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.ID, 'kc-login').click()
    driver.implicitly_wait(15)
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.XPATH,"//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div[1]/h2").text == "Синицина Инга"

# Позитивный тест на авторизацию по почте
# EXP-003

def test_authorization_tab_email():
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    # Вводим email
    pytest.driver.find_element(By.ID, 'username').send_keys('ingasinicina86@gmail.com')
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'password').send_keys('CevthrbVbhf-21586')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.ID, 'kc-login').click()
    driver.implicitly_wait(15)
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.XPATH,"//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div[1]/h2").text == "Синицина Инга"

# Негативный тест на авторизацию по email и появление сообщения о неверном логине и пароле. Элемент Забыл пароль перекрашивается в оранжевый цвет
# EXP-004

def test_authorization_tab_error_email():
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    # Вводим email
    pytest.driver.find_element(By.ID, 'username').send_keys('nochnoj-gost@yandex.ru')
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'password').send_keys('CevthrbVbhf-21586')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.ID, 'kc-login').click()
    driver.implicitly_wait(15)
    # Проверяем, что авторизация не прошла и появилось сообщение, а элемент Забыл пароль перекрашивается в оранжевый цвет.
    assert pytest.driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"
    assert pytest.driver.find_elements(By.CSS_SELECTOR, '#forgot_password-id .rt-link--orange-class')

# Позитивный тест на авторизацию по лицевому счету
# EXP-005

def test_authorization_tab_ls():
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    # Вводим ЛС
    pytest.driver.find_element(By.ID, 'username').send_keys('235010799317')
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'password').send_keys('CevthrbVbhf-21586')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.ID, 'kc-login').click()
    driver.implicitly_wait(15)
    # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element(By.XPATH,"//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div[1]/h2").text == "Синицина Инга"

# Негативный тест на авторизацию по лицевому счету
# EXP-006

def test_authorization_tab_error_ls():
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    # Вводим ЛС с ошибкой
    pytest.driver.find_element(By.ID, 'username').send_keys('235010ffh799')
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'password').send_keys('CevthrbVbhf-21586')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.ID, 'kc-login').click()
    driver.implicitly_wait(15)
    # Проверяем, что авторизация не прошла и появилось сообщение, а элемент Забыл пароль перекрашивается в оранжевый цвет.
    assert pytest.driver.find_element(By.ID, 'form-error-message').text == "Неверный логин или пароль"
    assert pytest.driver.find_elements(By.CSS_SELECTOR, '#forgot_password-id .rt-link--orange-class')

# Разрушающий тест на авторизацию по лицевому счету. Проверка работы ограничения на ввод 12 цифр в форме "ЛС".
# EXP-007

def test_authorization_tab_error_ls_12():
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    # Вводим ЛС с ошибкой (корректный ЛС + 3 лишних символа в конце)
    pytest.driver.find_element(By.ID, 'username').send_keys('235010799317123')
    # Вводим пароль
    pytest.driver.find_element(By.ID, 'password').send_keys('CevthrbVbhf-21586')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.ID, 'kc-login').click()
    driver.implicitly_wait(15)
    # Проверяем, что мы оказались на главной странице пользователя. Следовательно ограничение сработало, удалив лишние символы в конце ЛС.
    assert pytest.driver.find_element(By.XPATH, "//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div[1]/h2").text == "Синицина Инга"

# Позитивные тесты на автоматическую смену Таба:

# EXP-008
# (test_changing_the_authentication_tab_ls_phone упадет, на сайте баг)
def test_changing_the_authentication_tab_ls_phone():
    # Кликаем Таб выбора аутентификации по лицевому счету, он перекрашивется в оранжевый цвет
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-ls-id .rt-tab--active-class')
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-phone-id .rt-tab--small-class')
    # Вводим корректный phone
    pytest.driver.find_element(By.ID, 'username').send_keys('+79815045324')
    driver.implicitly_wait(5)
    # Наблюдаем, что Таб выбора аутентификации по телефону перекрашивется в оранжевый цвет, Таб выбора аутентификации по лицевому счету - черный. Проверяем:
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-ls-id .rt-tab--small-class')
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-phone-id .rt-tab--active-class')
    # Вводим корректный пароль
    pytest.driver.find_element(By.ID, 'password').send_keys('CevthrbVbhf-21586')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.ID, 'kc-login').click()
    driver.implicitly_wait(15)
    # Проверяем, что аутентификация прошла успешно
    assert pytest.driver.find_element(By.XPATH,"//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div[1]/h2").text == "Синицина Инга"

# EXP-009
# (test_changing_the_authentication_tab_ls_mail упадет, на сайте баг)
def test_changing_the_authentication_mail_ls_mail():
    # Кликаем Таб выбора аутентификации по лицевому счету, он перекрашивется в оранжевый цвет
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-ls-id .rt-tab--active-class')
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-mail-id .rt-tab--small-class')
    # Вводим корректный mail
    pytest.driver.find_element(By.ID, 'username').send_keys('ingasinicina86@gmail.com')
    driver.implicitly_wait(5)
    # Наблюдаем, что Таб выбора аутентификации по почте перекрашивется в оранжевый цвет, Таб выбора аутентификации по лицевому счету - черный. Проверяем:
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-ls-id .rt-tab--small-class')
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-mail-id .rt-tab--active-class')
    # Вводим корректный пароль
    pytest.driver.find_element(By.ID, 'password').send_keys('CevthrbVbhf-21586')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.ID, 'kc-login').click()
    driver.implicitly_wait(15)
    # Проверяем, что аутентификация прошла успешно
    assert pytest.driver.find_element(By.XPATH,"//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div[1]/h2").text == "Синицина Инга"

# EXP-010
def test_changing_the_authentication_tab_mail_phone():
    # Кликаем Таб выбора аутентификации по почте, он перекрашивется в оранжевый цвет
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-mail-id .rt-tab--active-class')
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-phone-id .rt-tab--small-class')
    # Вводим корректный phone
    pytest.driver.find_element(By.ID, 'username').send_keys('+79815045324')
    driver.implicitly_wait(5)
    # Наблюдаем, что Таб выбора аутентификации по телефону перекрашивется в оранжевый цвет, Таб выбора аутентификации по почте - черный. Проверяем:
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-mail-id .rt-tab--small-class')
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-phone-id .rt-tab--active-class')
    # Вводим коректный пароль
    pytest.driver.find_element(By.ID, 'password').send_keys('CevthrbVbhf-21586')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.ID, 'kc-login').click()
    driver.implicitly_wait(15)
    # Проверяем, что аутентификация прошла успешно
    assert pytest.driver.find_element(By.XPATH,"//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div[1]/h2").text == "Синицина Инга"

# EXP-011
def test_changing_the_authentication_tab_phone_mail():
    # Кликаем Таб выбора аутентификации по телефону, он перекрашивется в оранжевый цвет
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-phone-id .rt-tab--active-class')
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-mail-id .rt-tab--small-class')
    # Вводим корректный mail
    pytest.driver.find_element(By.ID, 'username').send_keys('ingasinicina86@gmail.com')
    driver.implicitly_wait(5)
    # Наблюдаем, что Таб выбора аутентификации по почте перекрашивется в оранжевый цвет, Таб выбора аутентификации по телефону - черный. Проверяем:
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-phone-id .rt-tab--small-class')
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-mail-id .rt-tab--active-class')
    # Вводим корректный пароль
    pytest.driver.find_element(By.ID, 'password').send_keys('CevthrbVbhf-21586')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.ID, 'kc-login').click()
    driver.implicitly_wait(15)
    # Проверяем, что аутентификация прошла успешно
    assert pytest.driver.find_element(By.XPATH,"//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div[1]/h2").text == "Синицина Инга"

# EXP-012
# (test_changing_the_authentication_tab_login_phone упадет, на сайте баг)
def test_changing_the_authentication_tab_login_phone():
    # Кликаем Таб выбора аутентификации по логину, он перекрашивется в оранжевый цвет
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-login-id .rt-tab--active-class')
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-phone-id .rt-tab--small-class')
    # Вводим корректный phone
    pytest.driver.find_element(By.ID, 'username').send_keys('+79815045324')
    driver.implicitly_wait(5)
    # Наблюдаем, что Таб выбора аутентификации по телефону перекрашивется в оранжевый цвет, Таб выбора аутентификации по логину - черный. Проверяем:
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-login-id .rt-tab--small-class')
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-phone-id .rt-tab--active-class')
    # Вводим корректный пароль
    pytest.driver.find_element(By.ID, 'password').send_keys('CevthrbVbhf-21586')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.ID, 'kc-login').click()
    driver.implicitly_wait(15)
    # Проверяем, что аутентификация прошла успешно
    assert pytest.driver.find_element(By.XPATH,"//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div[1]/h2").text == "Синицина Инга"

# EXP-013
def test_changing_the_authentication_tab_login_mail():
    # Кликаем Таб выбора аутентификации по логину, он перекрашивется в оранжевый цвет
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-login-id .rt-tab--active-class')
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-mail-id .rt-tab--small-class')
    # Вводим корректный mail
    pytest.driver.find_element(By.ID, 'username').send_keys('ingasinicina86@gmail.com')
    driver.implicitly_wait(5)
    # Наблюдаем, что Таб выбора аутентификации по почте перекрашивется в оранжевый цвет, Таб выбора аутентификации по логину - черный. Проверяем:
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-login-id .rt-tab--small-class')
    assert pytest.driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-mail-id .rt-tab--active-class')
    # Вводим корректный пароль
    pytest.driver.find_element(By.ID, 'password').send_keys('CevthrbVbhf-21586')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.ID, 'kc-login').click()
    driver.implicitly_wait(15)
    # Проверяем, что аутентификация прошла успешно
    assert pytest.driver.find_element(By.XPATH,"//*[@id="app"]/main/div/div[2]/div[1]/div[1]/div[1]/h2").text == "Синицина Инга"

# Проверка на корректность введенных данных в поле ввода имени при регистрации

# EXP-014
def test_registration_name_entry_field():
    # Нажимаем на кнопку Зарегистрироваться
    pytest.driver.find_element(By.ID, 'kc-register').click()
    # Вводим имя
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]').send_keys('Нина')
    # Ищем уведомление об ошибке
    err_name = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]')
    if err_name is None:
        print("test_registration_name_entry_field прошел успешно")
    else:
        print("test_registration_name_entry_field нашел баг")

# Проверка на корректность введенных данных в поле ввода имени при регистрации

# EXP-015
def test_registration_invalid_name_entry_field_a():
    # Нажимаем на кнопку Зарегистрироваться
    pytest.driver.find_element(By.ID, 'kc-register').click()
    # Вводим имя короче 2 букв
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]').send_keys('Н')
    # Ищем уведомление об ошибке
    assert pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]')

def test_registration_invalid_name_entry_field_b():
    # Нажимаем на кнопку Зарегистрироваться
    pytest.driver.find_element(By.ID, 'kc-register').click()
    # Вводим имя цифры
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]').send_keys('123')
    # Ищем уведомление об ошибке
    assert pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]')

def test_registration_invalid_name_entry_field_c():
    # Нажимаем на кнопку Зарегистрироваться
    pytest.driver.find_element(By.ID, 'kc-register').click()
    # Вводим имя длиннее 30 букв кириллицы
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]').send_keys('Аняманятанясаняванямашаглашаджек')
    # Ищем уведомление об ошибке
    assert pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]')

# EXP-016
def test_registration_invalid_name_the_input_field_is_empty():
    # Нажимаем на кнопку Зарегистрироваться
    pytest.driver.find_element(By.ID, 'kc-register').click()
    # Поле имени оставляем пустым
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]').send_keys(' ')
    # Вводим коректные данные в остальные поля формы регистрации
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]').send_keys('Козлова')
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/input[1]').send_keys('Москва')
    pytest.driver.find_element(By.ID, 'address').send_keys('89215045532')
    pytest.driver.find_element(By.ID, 'password').send_keys('9V3zywgyfq8D')
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys('9V3zywgyfq8D')
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/button[1]').click()
    # Ищем уведомление об ошибке
    assert pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]')

# EXP-017
# Проверка функции системы по сличению содержимого полей: Пароль и Подтверждение пароля
def test_registration_password_identity():
    # Нажимаем на кнопку Зарегистрироваться
    pytest.driver.find_element(By.ID, 'kc-register').click()
    # Вводим коректные данные в поля формы регистрации
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]').send_keys('Ира')
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]').send_keys('Козлова')
    pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/div[1]/input[1]').send_keys('Москва')
    pytest.driver.find_element(By.ID, 'address').send_keys('89215045532')
    pytest.driver.find_element(By.ID, 'password').send_keys('9V3zywgyfq8D')
    # Вводим в поле "Подтверждение пароля" данные, не соответствующие тем, которые введены в поле "Пароль"
    pytest.driver.find_element(By.ID, 'password-confirm').send_keys('9V3zywgyfq')
    # Ищем уведомление об ошибке
    err_name = pytest.driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]')
    if err_name is None:
        print("test_registration_password_identity нашел баг")
    else:
        print("test_registration_password_identity прошел успешно")
