import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: en-gb, ru, fr, de, es, it, sk, pt, ar, ca, cs, da, el, fi, ko, nl, pl, pt-br, ro, uk, zh-cn")

@pytest.fixture(scope="function")
def browser(request):
    lan = request.config.getoption("language")
    print("\nstart chrome browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lan})
    browser = webdriver.Chrome(options=options)  
    yield browser
    print("\nquit browser..")
    browser.quit()
    
