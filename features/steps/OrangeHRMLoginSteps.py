import os
from behave import given, when, then  # pylint: disable=no-name-in-module
from selenium import webdriver
from dotenv import load_dotenv
load_dotenv()


@when('enter username and password')
def enter_credentials(context):
    context.driver.find_element_by_id(
        "txtUsername").send_keys(os.getenv("USERNAME"))
    context.driver.find_element_by_id(
        "txtPassword").send_keys(os.getenv("PASSWORD"))


@when('click on login button')
def click_login_btn(context):
    context.driver.find_element_by_id("btnLogin").click()


@then('user should successfully login to the Dashboard page')
def verify_login(context):
    try:
        text = context.driver.find_element_by_xpath(
            "//h1[contains(text(),'Dashboard')]").text
    except:
        assert False, "Login Failed"
    assert text == "Dashboard"


@when('enter username "{username}" and password "{password}"')
def enter_credential_examples(context, username, password):
    context.driver.find_element_by_id(
        "txtUsername").send_keys(username)
    context.driver.find_element_by_id(
        "txtPassword").send_keys(password)
