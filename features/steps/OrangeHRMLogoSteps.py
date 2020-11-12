import os
from behave import given, when, then  # pylint: disable=no-name-in-module
from selenium import webdriver
from dotenv import load_dotenv
load_dotenv()


@then('verify logo is present on the page')
def verify_logo(context):
    status = context.driver.find_element_by_xpath(
        "//body/div[@id='wrapper']/div[@id='content']/div[@id='divLogin']/div[@id='divLogo']/img[1]").is_displayed()
    assert status is True
