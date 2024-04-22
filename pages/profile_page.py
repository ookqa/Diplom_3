import allure
from locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):

    @allure.step('Кликаем по кнопке перехода в раздел истории заказов')
    def click_order_history_button(self):
        locator = ProfilePageLocators.ORDER_HISTORY_BUTTON
        self.click_on_element(locator)

    @allure.step('Кликаем по кнопке выхода из аккаунта')
    def click_logout_button(self):
        locator = ProfilePageLocators.LOGOUT_BUTTON
        self.click_on_element(locator)

    @allure.step('Ожидаем появления секции информации о странице')
    def wait_for_about_section(self):
        locator = ProfilePageLocators.ABOUT
        self.find_element_with_wait(locator)

    @allure.step('Получаем текст секции с информацией о странице')
    def get_profile_page_info_section_text(self):
        title = ProfilePageLocators.ABOUT
        return self.get_text_from_element(title)
