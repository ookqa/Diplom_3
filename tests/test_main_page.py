import allure
import pytest
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from urls import Urls


class TestMainPage:

    @allure.title('Проверка перехода по клику на «Конструктор»')
    @allure.description('Проверяем переход к конструктору заказа по клику на кнопку из хэдера')
    def test_navigate_to_constructor_page(self, driver):
        driver.get(Urls.FEED_URL)
        main_page = MainPage(driver)
        main_page.click_header_constructor_button()
        main_page.wait_for_order_section()
        current_url = main_page.get_current_url()
        expect_constructor_section_text = main_page.get_constructor_title()

        assert current_url == 'https://stellarburgers.nomoreparties.site/' and 'Соберите бургер' in expect_constructor_section_text

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    @allure.description('Проверяем переход к ленте заказов по клику на кнопку из хэдера')
    def test_navigate_to_feed_page(self, driver):
        driver.get(Urls.MAIN_URL)
        main_page = MainPage(driver)
        main_page.click_header_feed_button()
        feed_page = FeedPage(driver)
        feed_page.wait_for_orders_list_section()
        current_url = main_page.get_current_url()
        expect_orders_list_text = feed_page.get_orders_list_title()

        assert current_url == Urls.FEED_URL and 'Лента заказов' in expect_orders_list_text

    @allure.title('Проверка открытия модалки ингредиента')
    @allure.description('Проверяем открытие модалки с деталями при клике на ингредиент')
    def test_ingredient_modal_window_is_open(self, driver):
        driver.get(Urls.MAIN_URL)
        main_page = MainPage(driver)
        main_page.click_ingredient_bun()
        main_page.wait_for_ingredient_modal()
        expected_ingredient_modal_text = main_page.get_ingredient_modal_title()

        assert 'Детали ингредиента' in expected_ingredient_modal_text

    @allure.title('Проверка закрытия модалки ингредиента')
    @allure.description('Проверяем закрытие модалки ингредиента при клике на крестик закрытия')
    def test_ingredient_modal_window_click_x_button_is_closed(self, driver):
        driver.get(Urls.MAIN_URL)
        main_page = MainPage(driver)
        main_page.click_ingredient_bun()
        main_page.wait_for_ingredient_modal()
        main_page.click_ingredient_modal_close_button()

        assert main_page.check_modal_window_is_closed()

    @allure.title('Проверка счетчика при добавлении ингредиента')
    @allure.description('Проверяем, что при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_check_ingredient_count_add_buns_counter_increase(self, driver, set_user_tokens):
        driver.get(Urls.MAIN_URL)
        main_page = MainPage(driver)
        ingr_count_before_add = main_page.get_ingredient_count_text()
        main_page.drag_ingredient_to_order_section()
        ingr_count_after_add = main_page.get_ingredient_count_text()

        assert int(ingr_count_before_add) < int(ingr_count_after_add)

    @allure.title('Проверка возможности создания заказа')
    @allure.description('Проверяем, что залогиненный пользователь может оформить заказ')
    def test_place_order_authorized_user(self, driver, set_user_tokens):
        driver.get(Urls.MAIN_URL)
        main_page = MainPage(driver)
        main_page.drag_ingredient_to_order_section()
        main_page.click_order_button()
        main_page.wait_for_created_order_modal()
        expected_order_modal_text = main_page.get_order_modal_title()

        assert 'идентификатор заказа' in expected_order_modal_text
