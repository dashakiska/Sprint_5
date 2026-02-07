from selenium.webdriver.common.by import By

class Locators:
    
    LOG_TO_ACC_BUTTON = (By.XPATH,"//button[text()='Войти в аккаунт']") #Кнопка Войти в аккаунт
    #EMAIL = [By.XPATH, "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input"]
    EMAIL = [By.XPATH, "//label[contains(text(),'Email')]/following-sibling::input"]
    PASSWORD = [By.XPATH, "//input[@type='password']"]
    NAME = [By.NAME, "name"]
    REG_BUTTON = (By.XPATH, "//a[@href='/register']") #Кнопка зарегистрироваться
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") #Кнопка зарегистрироваться на форме регистрации
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']") #Кнопка Войти на странице /login (main_site->Войти в аккаунт)
    RECOVER_LOGIN_LINK = (By.XPATH, "//a[text()='Войти']") #Кнопка Войти на восстановлении пароля
    ACCOUNT_BUTTON = [By.XPATH, "//p[text()='Личный Кабинет']"] #Кнопка личного кабинета на главной странице
    RECOVER_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']") #Кнопка восстaновить пароль
    KIT_BUTTON = (By.XPATH, "//p[text()='Конструктор']") #Кнопка Конструктор в шапке
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']") #Кнопка Выход в личном кабинете
    MODAL_OVERLAY = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr") #Модальное окно
    KIT_TAB = "tab_tab_type_current" #Активность
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div") #Таб Булки на главной
    SAUCE_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div") #Таб соусы
    FILLING_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div") #Таб начинки
    PASSWORD_ERROR = (By.CLASS_NAME, "input__error") #Ошибка пароля
