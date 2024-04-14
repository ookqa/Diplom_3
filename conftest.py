import pytest
import requests
from faker import Faker
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from urls import Urls

faker = Faker()


@pytest.fixture(scope='function')
def driver(request):
    driver_type = request.param
    if driver_type == 'chrome':
        options = Options()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif driver_type == 'firefox':
        options = Options()
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        driver = webdriver.Firefox()

    yield driver
    driver.quit()


@pytest.fixture()
def create_new_user():
    email = 'buntester' + faker.lexify(text='????????????') + '@bunstester.com'
    password = faker.lexify(text='????????????')
    name = faker.name()
    payload = {"email": email, "password": password, "name": name}
    response = requests.post(f"{Urls.REGISTER_USER}", data=payload)
    data = response.json()
    yield data
    access_token = data.get("accessToken")
    requests.delete(f"{Urls.DELETE_USER}", headers={'Authorization': f'{access_token}'})


@pytest.fixture()
def create_new_order(create_new_user):
    user_data = create_new_user
    access_token = user_data.get('accessToken')
    headers = {"Authorization": f"{access_token}"}
    payload = {
        'ingredients': ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa75', '61c0c5a71d1f82001bdaaa78']
    }
    requests.post(f'{Urls.GET_USER_ORDERS}', data=payload, headers=headers)


@pytest.fixture()
def set_user_tokens(driver, create_new_user):
    driver.get(Urls.MAIN_URL)
    user_data = create_new_user
    access_token = user_data.get('accessToken')
    refresh_token = user_data.get('refreshToken')
    driver.execute_script(f"window.localStorage.setItem('accessToken', '{access_token}');")
    driver.execute_script(f"window.localStorage.setItem('refreshToken', '{refresh_token}');")
