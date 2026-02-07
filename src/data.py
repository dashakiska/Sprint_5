import random

main_site = 'https://stellarburgers.education-services.ru/'

class Credentials:
    email = 'darya_menshchikova_37_126@mail.ru'
    password = '160484'
    name = 'Darya'
    rand_email = f"daria{random.randint(100, 999)}@yy.yu"
    short_password = '123'

timeout = 20  

class Endpoints:
    LOGIN = "/login"
    ACCOUNT = "/account"
    MAIN = "/" 