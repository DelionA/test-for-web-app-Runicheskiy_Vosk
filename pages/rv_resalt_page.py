from .base_page import BasePage
from pages.locators import RvResaltPageLocators
from pages.locators import RvMainPageLocators


class RvResaltPage(BasePage):
    # метод класса для проверки перенаправления на страницу
    def redirection_is_correct(self, url, title_expected):
        assert self.browser.current_url in url, \
            "должно перенаправлять на {}".format(url)
        assert self.browser.title in title_expected ,\
            "название страницы должно быть {}".format(title_expected)

    # метод класса для проверки заполненности полей значениями
    def fields_not_empty(self):
        field_number = 1
        for element in RvMainPageLocators.SELECTION_FIELDS:
            value_of_element = self.browser.find_element(*element).get_attribute('value')
            assert value_of_element != '', "поле {} не должно быть пустым".format(field_number)
            field_number += 1

    # метод класса для сопоставления фактического и ожидаемого значения поля
    def compare_expected_and_actual_value(self):
        field_number = 0
        for element in RvMainPageLocators.SELECTION_FIELDS:
            value_of_element = self.browser.find_element(*element).get_attribute('value')
            assert value_of_element == RvMainPageLocators.CORRECT_VALUES_LIST[field_number], \
                "значение поля {} не соответствует. должно быть {}".format(field_number, RvMainPageLocators.CORRECT_VALUES_LIST[field_number])
            field_number += 1

    # метод класса для проверки наличия полей описания сочетаний
    def should_be_fields_description(self):
        assert self.element_is_present(RvResaltPageLocators.FIELD_DESCRIPTION), \
            "отсутствует поле описания сочетаний Рун"

    # метод класса проверяет наличие 42 полей описания сочетаний
    def should_be_42_description_fields(self):
        fields = self.browser.find_elements(*RvResaltPageLocators.FIELD_DESCRIPTION)
        fields_count = len(fields)
        assert fields_count == 42, \
            "должно быть 42 поля описания сочетаний, а их {}".format(fields_count)

    # метод класса проверяет наличие кнопки 'Отправить'
    def button_send_is_present(self):
        assert self.element_is_present(RvResaltPageLocators.BUTTON_SEND),\
            "кнопка 'Отправить' отсутствует"

    def should_be_button_back(self):
        assert self.element_is_present(RvResaltPageLocators.BUTTON_BACK), \
            "кнопка 'Вернуться' отсутствует"
