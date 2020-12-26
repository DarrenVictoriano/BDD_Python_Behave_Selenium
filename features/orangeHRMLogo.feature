Feature: OrangeHRMLogo
    Scenario: Logo presence on OrangeHRM homepage
        Given launch chrome browser
        When open link "https://opensource-demo.orangehrmlive.com"
        Then verify logo is present on the page
        Then close chrome browser