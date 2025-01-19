import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeservice ## here naming this is important because i am using service class twice
from selenium.webdriver.firefox.service import Service as firefoxservice ## for two different browsers so it will create ambiguity & one won't work


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("--start-maximized")
        # chrome_option.add_argument("Headless")

        service_obj = chromeservice(r"F:\selenium_drivers\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj, options=chrome_option)
        # driver = webdriver.Chrome()

    elif browser_name == "firefox":
        firefox_option = webdriver.FirefoxOptions()
        firefox_option.add_argument("--start-maximized")

        service_obj = firefoxservice(r"F:\selenium_drivers\firefox\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj, options=firefox_option)

    request.cls.driver = driver
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    # driver.maximize_window()
    yield
    driver.close()
