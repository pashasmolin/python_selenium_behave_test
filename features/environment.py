from features.browser import Browser

from features.pages.dashboard_page import DashboardPage
from features.pages.login_page import LoginPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.dashboard_page = DashboardPage()


def after_all(context):
    context.browser.close()
