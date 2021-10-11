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
    url_resalt = 'http://localhost:5000/runicheskiyvosk_resalt/'
    runa = [
        'runa_1', 'runa_2', 'runa_3', 'runa_4',
        'runa_5', 'runa_6', 'runa_7'
    ]

    fields_selectors = (
        (By.CSS_SELECTOR, "#id_runa_1"),
        (By.CSS_SELECTOR, "#id_runa_2"),
        (By.CSS_SELECTOR, "#id_runa_3"),
        (By.CSS_SELECTOR, "#id_runa_4"),
        (By.CSS_SELECTOR, "#id_runa_5"),
        (By.CSS_SELECTOR, "#id_runa_6"),
        (By.CSS_SELECTOR, "#id_runa_7")
    )

    values_select = (
        ('uruz', 'uruz', 'thurisaz', 'ansuz', 'raido', 'kaunaz', 'gebo'),
        ('fehu', 'fehu', 'thurisaz', 'ansuz', 'raido', 'kaunaz', 'gebo'),
        ('fehu', 'uruz', 'fehu', 'ansuz', 'raido', 'kaunaz', 'gebo'),
        ('fehu', 'uruz', 'thurisaz', 'fehu', 'raido', 'kaunaz', 'gebo'),
        ('fehu', 'uruz', 'thurisaz', 'ansuz', 'fehu', 'kaunaz', 'gebo'),
        ('fehu', 'uruz', 'thurisaz', 'ansuz', 'raido', 'fehu', 'gebo'),
        ('fehu', 'uruz', 'thurisaz', 'ansuz', 'raido', 'kaunaz', 'fehu'),
    )

    values_select_id_8 = [
        'fehu', 'uruz', 'thurisaz', 'ansuz', 'raido', 'kaunaz', 'gebo'
    ]


    # ID_1 открытие страницы. url соответствует
    def test_open_page(self):
        self.open_page(self.url)
        assert self.browser.current_url == self.url,\
        "урл не соответствует ожидаемому"

    # ID_2 присутствует 7 полей выбора Рун
    def test_must_see_seven_fields(self):
        self.open_page(self.url)
        self.list_elements_in_present(self.fields_selectors)

    # ID_3 каждое из 7 полей содержит 24 варианта выбора Рун
    # переписать тест
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
        self.enter_values_in_fields(values_select, self.fields_selectors)

        field = (By.CSS_SELECTOR, "button")
        self.push_the_button(field)
        field_error = (By.CSS_SELECTOR, ".errorlist")
        assert self.element_is_present(field_error), "поле ошибок должно быть, но его нет."

    # ID_8 При уникальном выборе Рун перенаправляет на страницу результата
    def test_should_redirect_to_the_result_page(self):
        self. open_page(self.url)
        self.enter_values_in_fields(self.values_select_id_8, self.fields_selectors)

        field = (By.CSS_SELECTOR, "button")
        self.push_the_button(field)
        assert self.browser.current_url == self.url_resalt, "урл не соответствует, ожидаемый урл {}".format(self.url_resalt)

    # ID_9 Страница результата расклада РВ открывается
    @pytest.mark.xfail
    def test_the_page_should_not_open(self):
         # этот тест должен падать пока не переделаем вьюху
        self.open_page(self.url_resalt)
        assert self.browser.current_url != self.url_resalt, \
            "страница отображаться не должна, должно быть перенаправление на {}".format(self.url)

    # ID_10 На странице результата присутствует 7 полей с выбором Рун
    def test_must_see_seven_fields_in_result_page(self):
        self.open_page(self.url)
        self.enter_values_in_fields(self.values_select_id_8, self.fields_selectors)
        field = (By.CSS_SELECTOR, "button")
        self.push_the_button(field)
        assert self.browser.current_url == self.url_resalt, \
            "урл не соответствует, ожидаемый урл {}".format(self.url_resalt)
        self.list_elements_in_present(self.fields_selectors)

    # ID_11 На странице результата поля выбора Рун заполнены значениями
    def test_field_in_resalt_page_not_empty(self):
        self.open_page(self.url)
        self.enter_values_in_fields(self.values_select_id_8, self.fields_selectors)
        field = (By.CSS_SELECTOR, "button")
        self.push_the_button(field)
        self.fields_not_empty(self.fields_selectors)

    # Id_12 Заполненные значения в полях на странице результата расклада соответствуют
    def test_in_resalt_page_field_defined(self):
        self.open_page(self.url)
        self.enter_values_in_fields(self.values_select_id_8, self.fields_selectors)
        field = (By.CSS_SELECTOR, "button")
        self.push_the_button(field)
        self.compare_expected_and_actual_value(self.fields_selectors, self.values_select_id_8)

    # ID_13 Присутствует кнопка 'вернуться'
    def test_button_back_is_present(self):
        self.open_page(self.url)
        self.enter_values_in_fields(self.values_select_id_8, self.fields_selectors)
        field = (By.CSS_SELECTOR, "button")
        self.push_the_button(field)
        button_back = (By.XPATH, "/html/body/form[1]/button")
        assert self.element_is_present(button_back), "кнопка 'Вернуться' отсутствует"

    # ID_14 Присутствует кнопка 'отправить'
    def test_button_send_is_present(self):
        self.open_page(self.url)
        self.enter_values_in_fields(self.values_select_id_8, self.fields_selectors)
        field = (By.CSS_SELECTOR, "button")
        self.push_the_button(field)
        button_back = (By.XPATH, "/html/body/form[2]/button")
        assert self.element_is_present(button_back), "кнопка 'Отправить' отсутствует"

    # ID_15 На странице результата расклада присутствуют описания сочетаний Рун
    def test_description_of_combinations_in_resalt_page_is_present(self):
        self.open_page(self.url)
        self.enter_values_in_fields(self.values_select_id_8, self.fields_selectors)
        field = (By.CSS_SELECTOR, "button")
        self.push_the_button(field)
        field_description = (By.CSS_SELECTOR, ".card.container.mt-3")
        assert self.element_is_present(field_description), "отсутствует поле описания сочетаний Рун"

    # ID_16 На странице результата расклада присутствует 42 поля описания сочетаний Рун
    def test_fields_description_of_combinations_is_42(self):
        self.open_page(self.url)
        self.enter_values_in_fields(self.values_select_id_8, self.fields_selectors)
        field = (By.CSS_SELECTOR, "button")
        self.push_the_button(field)
        field_description = (By.CSS_SELECTOR, ".card.container.mt-3")
        fields = self.browser.find_elements(*field_description)
        fields_count = len(fields)
        assert fields_count == 42, "должно быть 42 поля описания сочетаний, а их {}".format(fields_count)


    # метод класса каждое поле заполнено значением
    def fields_not_empty(self, fields_selectors):
        field_number = 0
        for element in fields_selectors:
            value_of_element = self.browser.find_element(*element).get_attribute('value')
            assert value_of_element != '', "поле {} не должно быть пустым".format(field_number)
            field_number += 1

    # метод класса для сопоставления фактического и ожидаемого значения поля
    def compare_expected_and_actual_value(self, fields_selectors, values_select_id_8):
        field_number = 0
        for element in fields_selectors:
            value_of_element = self.browser.find_element(*element).get_attribute('value')
            assert value_of_element == values_select_id_8[field_number], \
                "значение поля {} не соответствует. должно быть {}".format(field_number, values_select_id_8[field_number])
            field_number += 1

    # метод класса для проверки наличия списка элементов на странице
    def list_elements_in_present(self, list_elements):
        field_number = 1
        for element in list_elements:
            assert self.element_is_present(element), "поле {} отсутствует".format(field_number)
            field_number += 1

    # метод класса для проверки наличия элемента на странице
    def element_is_present(self, field):
        try:
            if self.browser.find_element(*field):
                return True
        except:
            return False

    # метод класса заполняет семь полей значениями
    def enter_values_in_fields(self, values_list, elements_list):
        value_1, value_2, value_3,value_4, value_5, value_6, value_7 = values_list
        value_number = 0
        for element in elements_list:
            Select(self.browser.find_element(*element)).select_by_value(values_list[value_number])
            value_number += 1


    # метод класса для открытия страницы
    def open_page(self,url):
        self.browser.get(url)

    # метод класса найти элемент и "нажать" на него
    def push_the_button(self, field):
        element = self.browser.find_element(*field)
        element.click()
