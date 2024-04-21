import allure
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.order_history_page import OrderHistoryPage
from pages.profile_page import ProfilePage
import pytest
from urls import Urls


class TestFeedPage:

    @allure.title('Проверка модалки заказа')
    @allure.description('Проверяем, что если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_order_details_modal_appears(self, driver):
        driver.get(Urls.FEED_URL)
        feed_page = FeedPage(driver)
        feed_page.click_on_order_card()
        feed_page.wait_for_order_modal()
        expect_order_modal_title_text = feed_page.get_order_modal_title_text()

        assert 'бургер' in expect_order_modal_title_text

    @allure.title('Проверка заказов пользователя в "Ленте заказов"')
    @allure.description('Проверяем, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_navigate_to_order_history_page(self, driver, set_user_tokens, create_new_order):
        driver.get(Urls.MAIN_URL)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        feed_page = FeedPage(driver)
        order_history_page = OrderHistoryPage(driver)
        main_page.click_header_account_button()
        profile_page.wait_for_about_section()
        profile_page.click_order_history_button()
        order_history_page.wait_for_order_card()
        order_id = order_history_page.get_order_card_id_number_text()
        order_history_page.click_header_feed_button()
        feed_page.wait_for_orders_list_section()

        assert feed_page.check_feed_order_with_id(order_id)

    @allure.title('Проверка счетчика всех выполненных заказов')
    @allure.description('Проверяем, что при создании нового заказа счётчик "Выполнено за всё время" увеличивается')
    def test_total_orders_counter_increase(self, driver, set_user_tokens):
        driver.get(Urls.FEED_URL)
        feed_page = FeedPage(driver)
        feed_page.wait_for_orders_list_section()
        orders_count_before = feed_page.get_total_orders_count()
        feed_page.click_header_constructor_button()
        main_page = MainPage(driver)
        main_page.wait_for_order_section()
        main_page.drag_ingredient_to_order_section()
        main_page.click_order_button()
        main_page.wait_for_created_order_modal()
        main_page.click_ingredient_modal_close_button()
        main_page.click_header_feed_button()
        feed_page.wait_for_orders_list_section()
        orders_count_after = feed_page.get_total_orders_count()

        assert orders_count_before < orders_count_after

    @allure.title('Проверка счетчика заказов, выполненных сегодня')
    @allure.description('Проверяем, что при создании нового заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_today_orders_counter_increase(self, driver, set_user_tokens):
        driver.get(Urls.FEED_URL)
        feed_page = FeedPage(driver)
        feed_page.wait_for_orders_list_section()
        orders_count_before = feed_page.get_today_orders_count()
        feed_page.click_header_constructor_button()
        main_page = MainPage(driver)
        main_page.wait_for_order_section()
        main_page.drag_ingredient_to_order_section()
        main_page.click_order_button()
        main_page.wait_for_created_order_modal()
        main_page.click_ingredient_modal_close_button()
        main_page.click_header_feed_button()
        feed_page.wait_for_orders_list_section()
        orders_count_after = feed_page.get_today_orders_count()

        assert orders_count_before < orders_count_after

    @allure.title('Проверка заказа в работе')
    @allure.description('Проверяем, что после оформления заказа его номер появляется в разделе "В работе"')
    def test_new_order_appears_in_feed_progress_section(self, driver, set_user_tokens):
        driver.get(Urls.MAIN_URL)
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        main_page.wait_for_order_section()
        main_page.drag_ingredient_to_order_section()
        main_page.click_order_button()
        main_page.wait_for_new_order_modal_disapear()
        new_order_number = main_page.get_new_order_number_text()
        main_page.click_new_order_modal_close_button()
        main_page.click_header_feed_button()
        feed_page.wait_for_new_order_in_progress_section()

        assert feed_page.check_new_order_number_in_feed_progress_section(new_order_number)


