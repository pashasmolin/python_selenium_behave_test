from selenium.webdriver.common.by import By
from features.browser import Browser


class LoginPageLocator(object):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")


class LoginPage(Browser):

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def navigate(self, address):
        self.driver.get(address)

    def get_page_title(self):
        return self.driver.title

    def login(self, username, password):
        self.fill(username, *LoginPageLocator.USERNAME)
        self.fill(password, *LoginPageLocator.PASSWORD)
        self.click_element(*LoginPageLocator.SIGN_IN_BUTTON)