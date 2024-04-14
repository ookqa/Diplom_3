import allure
from locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    @allure.step('Ожидаем появления формы ввода нового пароля')
    def wait_for_new_password_form(self):
        locator = ResetPasswordPageLocators.NEW_PASSWORD_INPUT_FORM
        self.find_element_with_wait(locator)

    @allure.step('Получаем заголовка формы ввода нового пароля')
    def get_new_password_form_text(self):
        title = ResetPasswordPageLocators.NEW_PASSWORD_FORM_TITLE
        return self.get_text_from_element(title)

    @allure.step('Кликаем по кнопке "показать пароль" (глазик)')
    def click_eye_button(self):
        locator = ResetPasswordPageLocators.EYE_ICON
        self.click_on_element(locator)

    @allure.step('Ожидаем появления секции информации о странице')
    def check_new_password_form_is_highlight(self):
        locator = ResetPasswordPageLocators.PASSWORD_FIELD_ACTIVE
        self.find_element_with_wait(locator)
