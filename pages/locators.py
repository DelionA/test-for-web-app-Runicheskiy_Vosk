from selenium.webdriver.common.by import By

class RvMainPageLocators:
    BUTTON_SEND = (By.CSS_SELECTOR, "button")
    FIELD_ERRORLIST = (By.CSS_SELECTOR, ".errorlist")
    SELECTION_FIELDS = (
        (By.CSS_SELECTOR, "#id_runa_1"),
        (By.CSS_SELECTOR, "#id_runa_2"),
        (By.CSS_SELECTOR, "#id_runa_3"),
        (By.CSS_SELECTOR, "#id_runa_4"),
        (By.CSS_SELECTOR, "#id_runa_5"),
        (By.CSS_SELECTOR, "#id_runa_6"),
        (By.CSS_SELECTOR, "#id_runa_7")
    )

    INCORRECT_VALUES_LIST = (
        ('uruz', 'uruz', 'thurisaz', 'ansuz', 'raido', 'kaunaz', 'gebo'),
        ('fehu', 'fehu', 'thurisaz', 'ansuz', 'raido', 'kaunaz', 'gebo'),
        ('fehu', 'uruz', 'fehu', 'ansuz', 'raido', 'kaunaz', 'gebo'),
        ('fehu', 'uruz', 'thurisaz', 'fehu', 'raido', 'kaunaz', 'gebo'),
        ('fehu', 'uruz', 'thurisaz', 'ansuz', 'fehu', 'kaunaz', 'gebo'),
        ('fehu', 'uruz', 'thurisaz', 'ansuz', 'raido', 'fehu', 'gebo'),
        ('fehu', 'uruz', 'thurisaz', 'ansuz', 'raido', 'kaunaz', 'fehu')
    )

    CORRECT_VALUES_LIST = [
        'fehu', 'uruz', 'thurisaz', 'ansuz', 'raido', 'kaunaz', 'gebo'
    ]

class RvResaltPageLocators:
    BUTTON_SEND = (By.XPATH, "/html/body/form[2]/button")
    BUTTON_BACK = (By.XPATH, "/html/body/form[1]/button")
    FIELD_DESCRIPTION = (By.CSS_SELECTOR, ".card.container.mt-3")
