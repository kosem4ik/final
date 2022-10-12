import pytest
from selenium import webdriver
from Config.config import TestData


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
        web_driver.set_window_size(1400, 1000)

        request.cls.driver = web_driver
        yield
        web_driver.quit()
