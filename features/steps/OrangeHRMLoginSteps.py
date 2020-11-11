import os
from behave import given, when, then  # pylint: disable=no-name-in-module
from selenium import webdriver
from dotenv import load_dotenv
load_dotenv()


@given('1 launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(
        executable_path=os.getenv("CHROME_DRIVER_PATH"))


@when('1 open orangehrm homepage')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com")


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
    text = context.driver.find_element_by_xpath(
        "//h1[contains(text(),'Dashboard')]").text
    assert text == "Dashboard"


@then('close the browser')
def close_browser(context):
    context.driver.close()
