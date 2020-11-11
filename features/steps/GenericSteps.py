import os
from behave import given, when, then  # pylint: disable=no-name-in-module
from selenium import webdriver
from dotenv import load_dotenv
load_dotenv()


@given('launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(
        executable_path=os.getenv("CHROME_DRIVER_PATH"))


@when('open link "{link}"')
def open_link(context, link):
    context.driver.get(link)


@then('close chrome browser')
def close_browser(context):
    context.driver.close()
