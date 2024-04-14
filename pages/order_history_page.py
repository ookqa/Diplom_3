import allure
from locators import OrderHistoryPageLocators
from pages.base_page import BasePage


class OrderHistoryPage(BasePage):

    @allure.step('Ожидаем появления карточки заказа')
    def wait_for_order_card(self):
        locator = OrderHistoryPageLocators.ORDER_CARD
        self.find_element_with_wait(locator)

    @allure.step('Получаем текст карточки заказа')
    def get_order_card_text(self):
        title = OrderHistoryPageLocators.ORDER_CARD_TITLE
        return self.get_text_from_element(title)

    @allure.step('Получаем текст номера заказа в карточке')
    def get_order_card_id_number_text(self):
        title = OrderHistoryPageLocators.ORDER_CARD_ID_NUMBER
        return self.get_text_from_element(title)

    @allure.step('Кликам по кнопке "Лента заказов" в хэдере')
    def click_header_feed_button(self):
        self.click_on_element(OrderHistoryPageLocators.HEADER_FEED_BUTTON)
