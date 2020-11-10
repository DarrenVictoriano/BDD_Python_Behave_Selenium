import os
from behave import *
from selenium import webdriver
from dotenv import load_dotenv
load_dotenv()


@given('launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(
        executable_path=os.getenv("CHROME_DRIVER_PATH"))


@when('open orangehrm homepage')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com")


@then('verify logo is present on the page')
def verify_logo(context):
    status = context.driver.find_element_by_xpath(
        "//body/div[@id='wrapper']/div[@id='content']/div[@id='divLogin']/div[@id='divLogo']/img[1]").is_displayed()
    assert status is True


@then('close browser')
def close_browser(context):
    context.driver.close()
