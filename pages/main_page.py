import allure
from locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Кликаем по кнопке перехода в личный кабинет в хэдере')
    def click_header_account_button(self):
        locator = MainPageLocators.ACCOUNT_BUTTON
        self.click_on_element(locator)

    @allure.step('Кликам по кнопке "Конструктор" в хэдере')
    def click_header_constructor_button(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Кликам по кнопке "Лента заказов" в хэдере')
    def click_header_feed_button(self):
        self.click_on_element(MainPageLocators.HEADER_FEED_BUTTON)

    @allure.step('Кликам по ингредиенту (булочка)')
    def click_ingredient_bun(self):
        self.click_on_element(MainPageLocators.INGR_BUN)

    @allure.step('Кликам по крестику закрытия модалки с деталями ингредиента')
    def click_ingredient_modal_close_button(self):
        self.click_on_element(MainPageLocators.INGR_MODAL_CLOSE_BUTTON)

    @allure.step('Кликам по крестику закрытия модалки нового заказа')
    def click_new_order_modal_close_button(self):
        self.click_on_element(MainPageLocators.NEW_ORDER_MODAL_CLOSE_BUTTON)

    @allure.step('Кликам по кнопке оформления заказа')
    def click_order_button(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('Ожидаем появления секции конструктора заказов')
    def wait_for_order_section(self):
        locator = MainPageLocators.ORDER_SECTION
        self.find_element_with_wait(locator)

    @allure.step('Ожидаем появления секции конструктора заказов')
    def wait_for_new_order_modal(self):
        locator = MainPageLocators.GOT_NEW_ORDER_ID_MODAL
        self.find_element_with_wait(locator)

    @allure.step('Ожидаем получения номера нового заказа')
    def wait_for_new_order_modal_disapear(self):
        locator = MainPageLocators.NEW_ORDER_LOADING_MODAL
        self.check_element_is_invisible(locator)

    @allure.step('Ожидаем появления модалки с деталями ингредиента')
    def wait_for_ingredient_modal(self):
        locator = MainPageLocators.INGR_MODAL
        self.find_element_with_wait(locator)

    @allure.step('Ожидаем появления модалки с деталями заказа')
    def wait_for_created_order_modal(self):
        locator = MainPageLocators.ORDER_MODAL
        self.find_element_with_wait(locator)

    @allure.step('Получаем текст заголовка секции заказов')
    def get_constructor_title(self):
        title = MainPageLocators.CONSTRUCTOR_TITLE
        return self.get_text_from_element(title)

    @allure.step('Получаем текст заголовка модалки с деталями ингредиента')
    def get_ingredient_modal_title(self):
        title = MainPageLocators.INGR_MODAL_TITLE
        return self.get_text_from_element(title)

    @allure.step('Получаем текст заголовка модалки с деталями заказа')
    def get_order_modal_title(self):
        title = MainPageLocators.ORDER_MODAL_TITLE
        return self.get_text_from_element(title)

    @allure.step('Получаем текст заголовка секции заказов')
    def get_ingredient_count_text(self):
        text = MainPageLocators.BUNS_COUNT_IN_ORDER
        return self.get_text_from_element(text)

    @allure.step('Получаем номер заказа в модалке нового заказа')
    def get_new_order_number_text(self):
        text = MainPageLocators.NEW_ORDER_NUMBER
        return self.get_text_from_element(text)

    @allure.step('Перетаскиваем булочку в секцию заказа')
    def drag_ingredient_to_order_section(self):
        source = self.find_element_with_wait(MainPageLocators.INGR_BUN)
        target = self.find_element_with_wait(MainPageLocators.ORDER_SECTION)
        self.drag_and_drop_element(source, target)

    @allure.step('Проверяем закрытие модалки ингредиента')
    def check_modal_window_is_closed(self):
        return self.check_element_is_invisible(MainPageLocators.INGR_MODAL)
