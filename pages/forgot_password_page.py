import allure
from locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    @allure.step('Ожидаем появления формы восстановления пароля')
    def wait_for_password_recovery_form(self):
        locator = ForgotPasswordPageLocators.RECOVERY_FORM_TITLE
        self.find_element_with_wait(locator)

    @allure.step('Получаем текст заголовка формы восстановления пароля')
    def get_password_recovery_form_text(self):
        title = ForgotPasswordPageLocators.RECOVERY_FORM_TITLE
        return self.get_text_from_element(title)

    @allure.step('Нажимаем кнопку "Восстановить"')
    def click_password_recovery_button(self):
        locator = ForgotPasswordPageLocators.RECOVERY_BUTTON
        return self.click_on_element(locator)

    @allure.step('Устанавливаем email')
    def set_email(self, keys):
        element = ForgotPasswordPageLocators.EMAIL_FIELD
        self.find_element_with_wait(element).send_keys(keys)
