from selenium.webdriver.common.by import By
from features.browser import Browser


class DashboardPageLocator(object):
    DASHBOARD_MENU = (By.CSS_SELECTOR, "a[data-id='dashboard']")
    PASSWORD = (By.ID, "password")
    SIGN_IN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")


class DashboardPage(Browser):

    def get_page_title(self):
        return self.driver.title

