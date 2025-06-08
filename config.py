import generator


class LoginPageConfig:
    LOGIN_PAGE_URL = 'http://34.141.58.52:8080/#/login'
    EMAIL = 'fom@gmail.com'
    PASSWORD = 'qwert4321'
    EMAIL_MAIN = generator.random_email()
    PASSWORD_MAIN = generator.random_password()
class PetDetails:
    PET_NAME = generator.random_name(5)
    PET_VIEW = generator.random_view()
    PET_GENDER = generator.random_gender()
    PET_AGE = generator.random_age()
