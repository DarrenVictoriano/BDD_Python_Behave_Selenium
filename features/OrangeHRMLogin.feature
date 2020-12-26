Feature: OrangeHRMLogin
    Background: common steps
        Given launch chrome browser
        When open link "https://opensource-demo.orangehrmlive.com"

    Scenario: Login to OrangeHRM with valid account
        When enter valid username "admin" and password "admin123"
        And click on login button
        Then user should successfully login to the Dashboard page
        Then close chrome browser

    Scenario Outline: Login to OrangeHRM with Multiple parameters
        When enter username "<username>" and password "<password>"
        And click on login button
        Then user should successfully login to the Dashboard page
        Examples:
            | username | password |
            | admin    | admin123 |
            | admin123 | admin    |
            | adminxyz | admin123 |
            | admin    | adminxyz |