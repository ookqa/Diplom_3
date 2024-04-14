import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_history_page import OrderHistoryPage
from pages.profile_page import ProfilePage
import pytest
from urls import Urls


class TestProfilePage:

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка перехода по клику на «Личный кабинет»')
    @allure.description('Проверяем переход к личному кабинету по клику на кнопку из хэдера')
    def test_navigate_to_profile_page(self, driver, set_user_tokens):
        driver.get(Urls.MAIN_URL)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        main_page.click_header_account_button()
        profile_page.wait_for_about_section()
        current_url = profile_page.get_current_url()
        expect_about_text = profile_page.get_profile_page_info_section_text()

        assert current_url == Urls.PROFILE_URL and 'изменить свои персональные данные' in expect_about_text

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка перехода по клику на «История заказов»')
    @allure.description('Проверяем переход к истории заказов по клику на кнопку в меню')
    def test_navigate_to_order_history_page(self, driver, set_user_tokens, create_new_order):
        driver.get(Urls.MAIN_URL)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        order_history_page = OrderHistoryPage(driver)
        main_page.click_header_account_button()
        profile_page.wait_for_about_section()
        profile_page.click_order_history_button()
        order_history_page.wait_for_order_card()
        expect_order_card_text = order_history_page.get_order_card_text()
        current_url = order_history_page.get_current_url()

        assert current_url == Urls.ORDER_HISTORY_URL and 'бургер' in expect_order_card_text

    @pytest.mark.parametrize('driver', ['chrome', 'firefox'], indirect=True)
    @allure.title('Проверка выхода из аккаунта')
    @allure.description('Проверяем выхода из личного кабинета по клику на кнопку "Выход" из меню')
    def test_logout_from_profile_page(self, driver, set_user_tokens):
        driver.get(Urls.MAIN_URL)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        login_page = LoginPage(driver)
        main_page.click_header_account_button()
        profile_page.wait_for_about_section()
        profile_page.click_logout_button()
        login_page.wait_for_login_page_form_title()
        expect_login_page_title = login_page.get_login_page_form_title_text()
        current_url = login_page.get_current_url()

        assert current_url == Urls.LOGIN_ULR and 'Вход' in expect_login_page_title
