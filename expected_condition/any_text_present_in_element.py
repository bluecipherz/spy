from selenium.webdriver.support import expected_conditions as EC

class any_text_present_in_element(object):
    def __init__(self, location, text_):
        self.locator = locator
        self.text = text_

    def __call__(self, driver):
        try:
            element_text = EC._find_element(driver, self.locator).text
            return element_text != ''
        except StaleElementReferenceException:
            return False
