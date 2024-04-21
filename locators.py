from selenium.webdriver.common.by import By


class MainPageLocators:
    ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']/parent::a")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//li/a[@href='/']")
    CONSTRUCTOR_TITLE = (By.XPATH,
                         "//section[contains(@class, 'BurgerIngredients_ingredients')]/h1")
    HEADER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']/parent::a/parent::li")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_MODAL = (
    By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]/div[contains(@class, 'Modal_modal__container')]")
    ORDER_MODAL_TITLE = (By.XPATH,
                         "//section[contains(@class, 'Modal_modal_opened')]/div[contains(@class, 'Modal_modal__container')]//h2/following-sibling::p")
    INGR_BUN = (
    By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']/parent::a[contains(@class, 'BurgerIngredient_ingredient')]")
    BUNS_COUNT_IN_ORDER = (
    By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']//parent::a/div/p[contains(@class, 'counter')]")
    ORDER_SECTION = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]")
    INGR_MODAL = (
    By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]/div[contains(@class, 'Modal_modal__container')]")
    INGR_MODAL_CLOSE_BUTTON = (
    By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'close')]")
    INGR_MODAL_TITLE = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//h2")
    GOT_NEW_ORDER_ID_MODAL = (By.XPATH,
                              "//section[contains(@class, 'Modal_modal')]/following-sibling::div[contains(@class, 'Modal_modal')]/img[@alt='loading animation']")
    GOT_NEW_ORDER_ID_MODAL_INV = (By.XPATH, "//div[contains(@class, 'Modal_modal_opened')]")
    NEW_ORDER_NUMBER = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//h2")
    NEW_ORDER_LOADING_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//h2[text()='9999']")
    NEW_ORDER_MODAL_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'close')]")


class ProfilePageLocators:
    ABOUT = (By.XPATH, "//p[contains(@class, 'Account_text')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[@href='/account/order-history']")


class FeedPageLocators:
    ORDERS_LIST_SECTION = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]")
    ORDERS_LIST_TITLE = (By.XPATH, "//div[contains(@class, 'OrderFeed_orderFeed')]/h1")
    ORDER_IN_FEED = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')][1]")
    ORDER_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//div[contains(@class, 'Modal_orderBox')]")
    ORDER_MODAL_TITLE = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//div[contains(@class, 'Modal_orderBox')]//h2")
    TOTAL_ORDERS_COUNT = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS_COUNT = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    HEADER_CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    NEW_ORDER_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li")
    NEW_ORDER_NUMBER_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(@class, 'text_type_digits-default')]")


class LoginPageLocators:
    LOGIN_FORM_TITLE = (By.XPATH, "//div[contains(@class, 'Auth_login')]//h2")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")


class ForgotPasswordPageLocators:
    RECOVERY_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    RECOVERY_FORM_TITLE = (By.XPATH, "//div[contains(@class, 'Auth_login')]/h2")
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input")


class ResetPasswordPageLocators:
    EYE_ICON = (By.XPATH, "//div[@class='input__icon input__icon-action']/*[local-name() = 'svg']")
    NEW_PASSWORD_INPUT_FORM = (By.XPATH, "//input[@name='Введите новый пароль']")
    NEW_PASSWORD_FORM_TITLE = (By.XPATH, "//div[contains(@class, 'Auth_login')]/h2")
    PASSWORD_FIELD_ACTIVE = (By.XPATH, "//label[text()='Пароль']/parent::div[contains(@class, 'input_status_active')]")


class OrderHistoryPageLocators:
    ORDER_CARD = (By.XPATH, "//*[contains(@class, 'OrderHistory_listItem')]")
    ORDER_CARD_TITLE = (By.XPATH, "//*[contains(@class, 'OrderHistory_listItem')]//h2")
    ORDER_CARD_ID_NUMBER = (By.XPATH, "(//div[contains(@class, 'OrderHistory_textBox')]/p[contains(@class, 'text_type_digits-default')])[1]")
    HEADER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']/parent::a/parent::li")
