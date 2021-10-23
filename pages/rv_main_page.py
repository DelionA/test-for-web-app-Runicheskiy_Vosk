from .base_page import BasePage
from pages.locators import RvMainPageLocators


class RvMainPage(BasePage):
    def errorlist_not_present(self):
        assert not self.element_is_present(RvMainPageLocators.FIELD_ERRORLIST), \
            "поле ошибок не должно отображаться"
