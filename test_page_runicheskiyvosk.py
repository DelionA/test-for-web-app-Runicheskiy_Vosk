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
    runa = [
        'runa_1', 'runa_2', 'runa_3', 'runa_4',
        'runa_5', 'runa_6', 'runa_7'
    ]

    values_select = (
        ('uruz', 'uruz', 'thurisaz', 'ansuz', 'raido', 'kaunaz', 'gebo'),
        ('fehu', 'fehu', 'thurisaz', 'ansuz', 'raido', 'kaunaz', 'gebo'),
        ('fehu', 'uruz', 'fehu', 'ansuz', 'raido', 'kaunaz', 'gebo'),
        ('fehu', 'uruz', 'thurisaz', 'fehu', 'raido', 'kaunaz', 'gebo'),
        ('fehu', 'uruz', 'thurisaz', 'ansuz', 'fehu', 'kaunaz', 'gebo'),
        ('fehu', 'uruz', 'thurisaz', 'ansuz', 'raido', 'fehu', 'gebo'),
        ('fehu', 'uruz', 'thurisaz', 'ansuz', 'raido', 'kaunaz', 'fehu'),
      )

    # ID_1 открытие страницы. url соответствует
    def test_open_page(self):
        self.open_page(self.url)
        assert self.browser.current_url == self.url,\
        "урл не соответствует ожидаемому"

    # ID_2 присутствует 7 полей выбора Рун
    @pytest.mark.parametrize('runa', runa)
    def test_must_see_seven_fields(self, runa):
        selector = '#id_' + f"{runa}"
        field = (By.CSS_SELECTOR, selector)
        field_number = f"{runa}"[-1]
        assert  self.element_is_present(field),"поле {} не найдено".format(field_number)

    # ID_3 каждое из 7 полей содержит 24 варианта выбора Рун
    @pytest.mark.parametrize('runa', runa)
    def test_total_values_select_field(self, runa):
        selector = '#id_' + f"{runa}"
        field = (By.CSS_SELECTOR, selector)
        field_number = f"{runa}"[-1]
        element = self.browser.find_element(*field)
        select = Select(element)
        spisok = len(select.options)
        assert spisok - 1 == 24, 'выпадающий список поля {} не совпадает'.format(field_number)

    # ID_4 Отсутствует поле с предупреждением об уникальности выбора значения Рун
    def test_field_errors_not_present(self):
        field = (By.CSS_SELECTOR, ".errorlist")
        assert not self.element_is_present(field), "поле ошибок не должно отображаться"

    # ID_5 кнопка 'отправить' присутствует
    def test_sould_see_button_send(self):
        field = (By.CSS_SELECTOR, "button")
        assert self.element_is_present(field), "кнопка 'отправить' отстутствует"

    # ID_7 При неуникальных выбранных значениях Рун после нажатия
    # кнопки 'отправить' появляется предужпреждение
    @pytest.mark.parametrize('values_select', values_select)
    def test_should_see_field_error_if_not_unique_select_send_button(self, values_select):
        self.test_open_page()
        value_1, value_2, value_3,value_4, value_5, value_6, value_7 = values_select
        Select(self.browser.find_element(By.CSS_SELECTOR, "#id_runa_1")).select_by_value(value_1)
        Select(self.browser.find_element(By.CSS_SELECTOR, "#id_runa_2")).select_by_value(value_2)
        Select(self.browser.find_element(By.CSS_SELECTOR, "#id_runa_3")).select_by_value(value_3)
        Select(self.browser.find_element(By.CSS_SELECTOR, "#id_runa_4")).select_by_value(value_4)
        Select(self.browser.find_element(By.CSS_SELECTOR, "#id_runa_5")).select_by_value(value_5)
        Select(self.browser.find_element(By.CSS_SELECTOR, "#id_runa_6")).select_by_value(value_6)
        Select(self.browser.find_element(By.CSS_SELECTOR, "#id_runa_7")).select_by_value(value_7)
        field = (By.CSS_SELECTOR, "button")
        self.push_the_button(field)
        field_error = (By.CSS_SELECTOR, ".errorlist")
        assert self.element_is_present(field_error), "поле ошибок должно быть, но его нет."

    # метод класса для проверки наличия элемента на странице
    def element_is_present(self, field):
        try:
            if self.browser.find_element(*field):
                return True
        except:
            return False

    # метод класса для открытия страницы
    def open_page(self,url):
        self.browser.get(url)

    # метод класса найти элемент и "нажать" на него
    def push_the_button(self, field):
        element = self.browser.find_element(*field)
        element.click()
