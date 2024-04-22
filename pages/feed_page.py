import allure
from locators import FeedPageLocators
from locators import OrderHistoryPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):

    @allure.step('Ожидаем появления секции конструктора заказов')
    def wait_for_orders_list_section(self):
        locator = FeedPageLocators.ORDERS_LIST_SECTION
        self.find_element_with_wait(locator)

    @allure.step('Ожидаем появления номера заказа в секции выполнения заказов')
    def wait_for_new_order_in_progress_section(self):
        locator = FeedPageLocators.NEW_ORDER_IN_PROGRESS
        self.find_element_with_wait(locator)

    @allure.step('Ожидаем появления модалки с деталями заказа')
    def wait_for_order_modal(self):
        locator = FeedPageLocators.ORDER_MODAL
        self.find_element_with_wait(locator)

    @allure.step('Кликаем по верхнему заказу в ленте')
    def click_on_order_card(self):
        locator = FeedPageLocators.ORDER_IN_FEED
        self.click_on_element(locator)

    @allure.step('Кликам по кнопке "Конструктор" в хэдере')
    def click_header_constructor_button(self):
        self.click_on_element(FeedPageLocators.HEADER_CONSTRUCTOR_BUTTON)

    @allure.step('Получаем текст заголовка секции заказов')
    def get_orders_list_title(self):
        title = FeedPageLocators.ORDERS_LIST_TITLE
        return self.get_text_from_element(title)

    @allure.step('Получаем текст заголовка модалки с деталями заказа')
    def get_order_modal_title_text(self):
        title = FeedPageLocators.ORDER_MODAL_TITLE
        return self.get_text_from_element(title)

    @allure.step('Получаем количество заказов, выполненных за все время')
    def get_total_orders_count(self):
        title = FeedPageLocators.TOTAL_ORDERS_COUNT
        return self.get_text_from_element(title)

    @allure.step('Получаем количество заказов, выполненных за сегодня')
    def get_today_orders_count(self):
        title = FeedPageLocators.TODAY_ORDERS_COUNT
        return self.get_text_from_element(title)

    @allure.step('Проверяем наличие в ленте заказа с номером из истории заказа пользователя')
    def check_feed_order_with_id(self, order_id):
        locator = OrderHistoryPageLocators.ORDER_CARD_ID_NUMBER
        xpath_with_text = f"{locator[1]}[contains(text(), '{order_id}')]"
        locator_with_text = (locator[0], xpath_with_text)
        return self.find_element_with_wait(locator_with_text)

    @allure.step('Проверяем наличие в разделе "В работе" номер нового заказа')
    def check_new_order_number_in_feed_progress_section(self, new_order_number):
        locator = FeedPageLocators.NEW_ORDER_NUMBER_IN_PROGRESS
        xpath_with_text = f"{locator[1]}[contains(normalize-space(), '{new_order_number}')]"
        locator_with_text = (locator[0], xpath_with_text)
        return self.find_element_with_wait(locator_with_text)
