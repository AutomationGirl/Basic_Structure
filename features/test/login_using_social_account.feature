Feature: Login functionality by using social account

  Background:

    When Open the Radius url
    And Navigate to Log In page

  Scenario: login with valid gmail credentials

    When Login through Google sign in
    When Enter valid gmail email id as shivani@gmail.com
    And Enter valid gmail password
    And Click allow access button
    Then I see network page


 Scenario: login with valid RRC credentials

    When Login through RRC sign in
    Then See the RRC login page
    When Enter email id as shivani@gmail.com
    And Enter password
    And Click on login RRC button
    Then I see error page
