from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import Select
from pages.locators import RvMainPageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    # метод класса открывает страницу
    def open_page(self):
        self.browser.get(self.url)

    # метод класса нажимает кнопку 'Отправить'
    def push_button_send(self):
        self.browser.find_element(*RvMainPageLocators.BUTTON_SEND).click()

    # метод класса проверяет соответствие текущего урла ожидаемому
    def url_match(self, url_expected):
        assert url_expected in  self.browser.current_url,\
            "урл не соответствует ожидаемому"

    # метод класса проверяет соответствие названия страницы ожидаемому
    def title_match(self, title_expected):
        assert title_expected == self.browser.title,\
            "название страницы не соответствует ожидаемому"

    # метод класса проверяет наличие элемента на странице
    def element_is_present(self, field):
        try:
            if self.browser.find_element(*field):
                return True
        except:
            return False

    # метод класса проверяет наличие семи полей селект на странице
    def should_be_seven_fields(self):
        field_number = 1
        for element in RvMainPageLocators.SELECTION_FIELDS:
            assert self.element_is_present(element), \
                "поле {} отсутствует".format(field_number)
            field_number += 1

    # метод класса проверяет наличие поля ошибок
    def should_bee_field_errors(self):
        assert self.element_is_present(RvMainPageLocators.FIELD_ERRORLIST), \
            "предупреждение о неуникальности значений отсутствует"

    # метод класса проверяет наличие у каждого поля селект 24 варианта выбора
    def each_field_contain_24_values(self):
        field_number = 1
        for element in RvMainPageLocators.SELECTION_FIELDS:
            select = Select(self.browser.find_element(*element))
            count_values = len(select.options) - 1
            assert count_values == 24, \
                'поле {} должно содержать 24 варианта выбора значения'.format(field_number)
            field_number += 1

    # метод класса проверяет наличие кнопки 'Отправить'
    def button_send_is_present(self):
        assert self.element_is_present(RvMainPageLocators.BUTTON_SEND),\
            "кнопка 'Отправить' отсутствует"

    # метод класса заполняет поля выбора Рун данными
    def enter_values_in_fields(self, values_list):
        value_number = 0
        for element in RvMainPageLocators.SELECTION_FIELDS:
            Select(self.browser.find_element(*element)).select_by_value(values_list[value_number])
            value_number += 1
