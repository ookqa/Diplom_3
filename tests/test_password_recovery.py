import allure
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
import pytest
from pages.reset_password_page import ResetPasswordPage
from urls import Urls


class TestPasswordRecovery:

    @allure.title('Проверка перехода на страницу восстановления пароля')
    @allure.description('Проверяем переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_navigate_to_password_recovery_page(self, driver):
        driver.get(Urls.LOGIN_ULR)
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)
        login_page.click_password_recovery_link()
        forgot_password_page.wait_for_password_recovery_form()
        expect_password_recovery_form_title = forgot_password_page.get_password_recovery_form_text()
        current_url = forgot_password_page.get_current_url()

        assert current_url == Urls.FORGOT_PASSWORD_URL and 'Восстановление пароля' in expect_password_recovery_form_title

    @allure.title('Проверка ввода почты для восстановления')
    @allure.description('Проверяем ввод почты и клик по кнопке «Восстановить»')
    def test_input_email_and_click_recovery_button(self, driver):
        driver.get(Urls.FORGOT_PASSWORD_URL)
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.wait_for_password_recovery_form()
        forgot_password_page.set_email('buntester@testbuns.com')
        forgot_password_page.click_password_recovery_button()
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.wait_for_new_password_form()
        expect_new_password__form_title = reset_password_page.get_new_password_form_text()
        current_url = reset_password_page.get_current_url()

        assert current_url == Urls.RESET_PASSWORD_URL and 'Восстановление пароля' in expect_new_password__form_title

    @allure.title('Проверка кнопки "показать пароль"')
    @allure.description('Проверяем, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_input_email_click_eye_button_highlight_field(self, driver):
        driver.get(Urls.FORGOT_PASSWORD_URL)
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.wait_for_password_recovery_form()
        forgot_password_page.set_email('buntester@testbuns.com')
        forgot_password_page.click_password_recovery_button()
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.wait_for_new_password_form()
        reset_password_page.click_eye_button()

        assert reset_password_page.check_new_password_form_is_highlight() == True
