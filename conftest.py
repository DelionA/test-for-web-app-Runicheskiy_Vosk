import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def browser():
    print('\nStart Firefox browser for test...')
    browser = webdriver.Firefox()
    yield browser
    print('\nQuit Firefox browser')
    browser.quit()
