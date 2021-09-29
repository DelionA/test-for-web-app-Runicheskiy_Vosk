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

    # тест открытие страницы. урл соответствует
    def test_open_page(self):
        self.open_page(self.url)
        assert self.browser.current_url == self.url,\
        "урл не соответствует ожидаемому"

    # тест поле селект присутствует
    @pytest.mark.parametrize('runa', runa)
    def test_must_see_seven_fields(self, runa):
        selector = '#id_' + f"{runa}"
        field = (By.CSS_SELECTOR, selector)
        field_number = f"{runa}"[-1]
        assert  self.element_is_present(field),"поле {} не найдено".format(field_number)

    # тест поле содержит 24 значения селект
    @pytest.mark.parametrize('runa', runa)
    def test_total_values_select_field(self, runa):
        selector = '#id_' + f"{runa}"
        field = (By.CSS_SELECTOR, selector)
        field_number = f"{runa}"[-1]
        element = self.browser.find_element(*field)
        select = Select(element)
        spisok = len(select.options)
        assert spisok - 1 == 24, 'выпадающий список поля {} не совпадает'.format(field_number)

    # тест кнопка 'отправить' присутствует
    def test_sould_see_button_send(self):
        field = (By.CSS_SELECTOR, "button")
        assert self.element_is_present(field), "кнопка 'отправить' отстутствует"

    # туст поле ошибок отсутствует
    def test_field_errors_not_present(self):
        field = (By.CSS_SELECTOR, ".errorlist")
        assert not self.element_is_present(field), "поле ошибок не должно отображаться"

    
    # метод класса найти элемент и "нажать" на него
    def push_the_button(self, field):
        element = self.browser.find_element(*field)
        element.click()

    # метод класса для проверки наличия элемента на странице
    def element_is_present(self, field):
        try:
            if self.browser.find_element(*field):
                return True
        except:
            return False

    #метод класса для открытия страницы
    def open_page(self,url):
        self.browser.get(url)
