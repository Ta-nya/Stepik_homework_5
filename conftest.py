import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# обработка командной строки - '--browser_name' - название параметра который можно вводить в командную строку
# default=None - можно поставить значение по умолчанию
def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default=None,
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default='en-gb',
                     help="Choose browser: chrome or firefox")

@pytest.fixture(scope="function")
def browser(request):
    # проверка что текущий браузер chrome or firefox
    browser = request.config.getoption("browser")
    browser = None
    if browser == "chrome" or "Chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser == "firefox" or "Firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("--language")
    print(f"\nstart browser for test in {user_language}")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    link = f"http://selenium1py.pythonanywhere.com/{user_language}/accounts/login/"
    browser.get(link)
    browser.maximize_window()
    time.sleep(1)
    yield browser
    print("\nquit browser..")
    browser.quit()
