from behave import step
from nose.tools import assert_equal, assert_true


@step('I navigate to the Livongo Login page')
def step_impl(context):
    context.login_page.navigate("https://my.livongo.com/login")
    assert_equal(context.login_page.get_page_title(), "Sign into your account - Livongo Health")


@step('I login with username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)


@step('I am taken to the Livongo Dashboard page')
def step_impl(context):
    context.dashboard_page.get_page_title()
    assert_true(context.dashboard_page.get_page_title(), "Dashboard - Livongo Health")

