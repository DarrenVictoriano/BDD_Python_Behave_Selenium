Feature: OrangeHRM Logo
    Scenario: Logo presence on OrangeHRM homepage
        Given launch chrome browser
        When open orangehrm homepage
        Then verify logo is present on the page
        And close browser