from selenium.webdriver.common.by import By

class Locators:
    #registration locators
    LOG_TO_ACC_BUTTON = (By.XPATH,"//button[text()='Войти в аккаунт']") #Кнопка Войти в аккаунт
    EMAIL = [By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input"]
    PASSWORD = [By.XPATH, "//input[@type='password']"]
    NAME = [By.NAME, "name"]
    REG_BUTTON = (By.XPATH, "//a[@href='/register']") #Кнопка зарегистрироваться
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")#Кнопка зарегистрироваться на форме регистрации
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']")#Кнопка Войти на странице /login (main_site->Войти в аккаунт)
    ACCOUNT_BUTTON = [By.XPATH, "//p[text()='Личный Кабинет']"]#Кнопка личного кабинета на главной странице
    RECOVER_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")#Кнопка восстaновить пароль
    KIT_BUTTON = (By.XPATH, "//p[text()='Конструктор']")#Кнопка Конструктор в шапке
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")#Кнопка Выход в личном кабинете
    MODAL_OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")#Модальное окно
    BUNS_BUTTON = (By.XPATH, "//span[text()='Булки']")#Кнопка Булки на главной
    SAUCE_BUTTON = (By.XPATH, "//span[text()='Соусы']")#Кнопка соусы
    FILLING_BUTTON = (By.XPATH, "//span[text()='Начинки']")#Кнопка начинки
    TEXT_BUNS = (By.XPATH, "//h2[text()='Булки']")#Раздел булки в конструкторе
    TEXT_SAUCE = (By.XPATH, "//h2[text()='Соусы']")#Раздел соусы в конструкторе
    TEXT_FILLING = (By.XPATH, "//h2[text()='Начинки']")#Раздел начинки в конструкторе

