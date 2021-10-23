import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.rv_main_page import RvMainPage
from pages.rv_resalt_page import RvResaltPage
from pages.base_page import BasePage
from pages.locators import RvMainPageLocators
from pages.locators import RvResaltPageLocators


url = 'localhost:5000/runicheskiyvosk'
url_resalt = 'http://localhost:5000/runicheskiyvosk_resalt/'
title_rv_main_page = 'some title'
title_rv_result_page = 'RunicheskiyVosk - Resalt'


class TestRvMainPage:
    # ID_1 открытие страницы. url и title соответствуют
    def test_open_rv_main_page(self, browser):
        page = RvMainPage(browser, url)
        page.open_page()
        page.url_match(url)
        page.title_match(title_rv_main_page)

    # ID_2 присутствует 7 полей выбора Рун
    def test_must_see_seven_fields(self, browser):
        page = RvMainPage(browser, url)
        page.open_page()
        page.should_be_seven_fields()

    # ID_3 каждое из 7 полей содержит 24 варианта выбора Рун
    def test_each_field_must_contain_24_values(self, browser):
        page = RvMainPage(browser, url)
        page.open_page()
        page.each_field_contain_24_values()

    # ID_4 Отсутствует поле с предупреждением об уникальности выбора значения Рун
    def test_field_errors_not_present(self, browser):
        page = RvMainPage(browser, url)
        page.open_page()
        page.errorlist_not_present()

    # ID_5 кнопка 'отправить' присутствует
    def test_sould_see_button_send(self, browser):
        page = RvMainPage(browser, url)
        page.open_page()
        page.button_send_is_present()

    # ID_7 При неуникальных выбранных значениях Рун после нажатия
    # кнопки 'отправить' появляется предужпреждение
    @pytest.mark.parametrize("values_list", RvMainPageLocators.INCORRECT_VALUES_LIST)
    def test_should_see_field_error(self, browser, values_list):
        page = RvMainPage(browser, url)
        page.open_page()
        page.enter_values_in_fields(values_list)
        page.push_button_send()
        page.url_match(url)
        page.should_bee_field_errors()

    # ID_8 При уникальном выборе Рун перенаправляет на страницу результата
    def test_should_redirect_to_the_result_page(self, browser):
        page = RvMainPage(browser, url)
        page.open_page()
        page.enter_values_in_fields(RvMainPageLocators.CORRECT_VALUES_LIST)
        page.push_button_send()
        page.url_match(url_resalt)


class TestRvResaltPage:
    # ID_9 Страница результата расклада РВ открывается
    # этот тест должен падать пока не переделаем вьюху
    @pytest.mark.xfail
    def test_should_redirect_to_the_main_page(self,browser):
        page = RvResaltPage(browser, url)
        page.open_page()
        page.redirection_is_correct(url, title_rv_main_page)

    # ID_10 На странице результата присутствует 7 полей с выбором Рун
    def test_must_see_seven_fields_in_result_page(self, browser):
        page = RvResaltPage(browser, url)
        page.open_page()
        page.enter_values_in_fields(RvMainPageLocators.CORRECT_VALUES_LIST)
        page.push_button_send()
        page.redirection_is_correct(url_resalt, title_rv_result_page)
        page.should_be_seven_fields()

    # ID_11 На странице результата поля выбора Рун заполнены значениями
    def test_field_in_resalt_page_not_empty(self, browser):
        page = RvResaltPage(browser, url)
        page.open_page()
        page.enter_values_in_fields(RvMainPageLocators.CORRECT_VALUES_LIST)
        page.push_button_send()
        page.redirection_is_correct(url_resalt, title_rv_result_page)
        page.fields_not_empty()

    # Id_12 Заполненные значения в полях на странице результата расклада соответствуют
    def test_in_resalt_page_field_defined(self, browser):
        page = RvResaltPage(browser, url)
        page.open_page()
        page.enter_values_in_fields(RvMainPageLocators.CORRECT_VALUES_LIST)
        page.push_button_send()
        page.redirection_is_correct(url_resalt, title_rv_result_page)
        page.compare_expected_and_actual_value()

    # ID_13 Присутствует кнопка 'Вернуться'
    def test_button_back_is_present(self, browser):
        page = RvResaltPage(browser, url)
        page.open_page()
        page.enter_values_in_fields(RvMainPageLocators.CORRECT_VALUES_LIST)
        page.push_button_send()
        page.redirection_is_correct(url_resalt, title_rv_result_page)
        page.should_be_button_back()

    # ID_14 Присутствует кнопка 'Отправить'
    def test_button_send_is_present(self, browser):
        page = RvResaltPage(browser, url)
        page.open_page()
        page.enter_values_in_fields(RvMainPageLocators.CORRECT_VALUES_LIST)
        page.push_button_send()
        page.redirection_is_correct(url_resalt, title_rv_result_page)
        page.button_send_is_present()

    # ID_15 На странице результата расклада присутствуют описания сочетаний Рун
    def test_description_of_combinations_in_resalt_page_is_present(self, browser):
        page = RvResaltPage(browser, url)
        page.open_page()
        page.enter_values_in_fields(RvMainPageLocators.CORRECT_VALUES_LIST)
        page.push_button_send()
        page.redirection_is_correct(url_resalt, title_rv_result_page)
        page.should_be_fields_description()

    # ID_16 На странице результата расклада присутствует 42 поля описания сочетаний Рун
    def test_fields_description_of_combinations_is_42(self, browser):
        page = RvResaltPage(browser, url)
        page.open_page()
        page.enter_values_in_fields(RvMainPageLocators.CORRECT_VALUES_LIST)
        page.push_button_send()
        page.redirection_is_correct(url_resalt, title_rv_result_page)
        page.should_be_42_description_fields()
