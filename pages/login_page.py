import allure
from locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Кликаем по ссылке восстановления пароль')
    def click_password_recovery_link(self):
        locator = LoginPageLocators.FORGOT_PASSWORD_LINK
        self.click_on_element(locator)

    @allure.step('Ожидаем появления заголовка формы логина')
    def wait_for_login_page_form_title(self):
        locator = LoginPageLocators.LOGIN_FORM_TITLE
        self.find_element_with_wait(locator)

    @allure.step('Получаем текст заголовка формы логина')
    def get_login_page_form_title_text(self):
        title = LoginPageLocators.LOGIN_FORM_TITLE
        return self.get_text_from_element(title)
