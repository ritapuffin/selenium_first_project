from selenium.common.exceptions import NoSuchElementException

class BasePage(object):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(10)

    def open(self): 
        self.browser.get(self.url)
        
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
        
    def is_url_contains_correct_substring(self, substring_to_search):
        if substring_to_search in self.browser.current_url:
            return True
        return False
        