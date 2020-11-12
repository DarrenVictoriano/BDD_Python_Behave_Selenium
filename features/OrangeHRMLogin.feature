Feature: OrangeHRMLogin
    Scenario: Login to OrangeHRM with valid account
        Given launch chrome browser
        When open link "https://opensource-demo.orangehrmlive.com"
        And enter username and password
        And click on login button
        Then user should successfully login to the Dashboard page
        Then close chrome browser

    Scenario Outline: Login to OrangeHRM with Multiple parameters
        Given launch chrome browser
        When open link "https://opensource-demo.orangehrmlive.com"
        And enter username "<username>" and password "<password>"
        And click on login button
        Then user should successfully login to the Dashboard page

        Examples:
            | username | password |
            | admin    | admin123 |
            | admin123 | admin    |
            | adminxyz | admin123 |
            | admin    | adminxyz |