import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Base:
    def setup_class(self):
        print('\nstart browser Firefox')
        self.browser = webdriver.Firefox()

    def teardown_class(self):
        print('\nquit browser Firefox')
        self.browser.quit()


class TestRvPage(Base):
    # класс тест страницы htttp://site/runicheskiyvosk
    url = 'http://localhost:5000/runicheskiyvosk/'

    # тест открытие страницы. урл соответстовует
    def test_open_page(self):
        self.open_page(self.url)
        assert self.browser.current_url == self.url,\
        "урл не соответствует ожидаемому"

    def test_must_see_seven_fields(self):
        # поле 1
        field_1 = (By.CSS_SELECTOR, "#id_runa_1")
        assert  self.find_element_(field_1),"поле 1 не найдено"
        # проверить что поле 1 содержит 24 селект
        element = self.browser.find_element_by_css_selector('#id_runa_1')
        select = Select(element)
        spisok = len(select.options)
        assert spisok - 1 == 24, 'выпадающий список поля 1 не совпадает'


        # поле 2
        field_2 = (By.CSS_SELECTOR, "#id_runa_2")
        assert  self.find_element_(field_2),"поле 2 не найдено"
        # проверить что поле 2 содержит 24 селект
        element = self.browser.find_element_by_css_selector('#id_runa_2')
        select = Select(element)
        spisok = len(select.options)
        assert spisok - 1 == 24, 'выпадающий список поля 2 не совпадает'

        # поле 3
        field_3 = (By.CSS_SELECTOR, "#id_runa_3")
        assert  self.find_element_(field_3),"поле 3 не найдено"
        element = self.browser.find_element_by_css_selector('#id_runa_3')
        select = Select(element)
        spisok = len(select.options)
        assert spisok - 1 == 24, 'выпадающий список поля 3 не совпадает'

        # поле 4
        field_4 = (By.CSS_SELECTOR, "#id_runa_4")
        assert  self.find_element_(field_4),"поле 4 не найдено"
        element = self.browser.find_element_by_css_selector('#id_runa_4')
        select = Select(element)
        spisok = len(select.options)
        assert spisok - 1 == 24, 'выпадающий список поля 4 не совпадает'

        # поле 5
        field_5 = (By.CSS_SELECTOR, "#id_runa_5")
        assert  self.find_element_(field_5),"поле 5 не найдено"
        element = self.browser.find_element_by_css_selector('#id_runa_5')
        select = Select(element)
        spisok = len(select.options)
        assert spisok - 1 == 24, 'выпадающий список поля 5 не совпадает'

        # поле 6
        field_6 = (By.CSS_SELECTOR, "#id_runa_6")
        assert  self.find_element_(field_6),"поле 6 не найдено"
        element = self.browser.find_element_by_css_selector('#id_runa_6')
        select = Select(element)
        spisok = len(select.options)
        assert spisok - 1 == 24, 'выпадающий список поля 6 не совпадает'

        # поле 7
        field_7 = (By.CSS_SELECTOR, "#id_runa_7")
        assert  self.find_element_(field_7),"поле 7 sне найдено"
        element = self.browser.find_element_by_css_selector('#id_runa_7')
        select = Select(element)
        spisok = len(select.options)
        assert spisok - 1 == 25, 'выпадающий список поля 7 не совпадает'

    # метод класса для проверки наличия элемента на странице
    def find_element_(self, field):
        try:
            if self.browser.find_element(*field):
                return True
        except:
            return False

    #метод класса для открытия страницы
    def open_page(self,url):
        self.browser.get(url)
