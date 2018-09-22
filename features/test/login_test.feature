Feature: Login functionality by using email id and password

  Background:

    When Open the Radius url
    And Navigate to Log In page


  Scenario: login with valid credentials

    When Enter valid email id as Shivani@gmail.com
    And Enter valid password
    And Click on login button

    Then I see network page
    And Click on logout button


  Scenario: login with invalid credentials

    When Enter invalid email id as dummy@gmail.com
    And Enter invalid password
    And Click on login button

    Then I see error message


  Scenario: login with valid email id and invalid password

    When Enter valid email id as Shivani@gmail.com
    And Enter invalid password
    And Click on login button

    Then I see error message

  Scenario: login with invalid email id and valid password

    When Enter invalid email id as dummy@gmail.com
    And Enter invalid password
    And Click on login button

    Then I see error message

  Scenario: login with blank email id and blank password

    When Click on login button
    Then I see validation message

 Scenario: Clicking on forget password link with valid email id


    When I click on forget password link
    Then I redirect forget password page

    And Enter email id and click on reset email button
    Then See the success message

  Scenario: Clicking on forget password link with blank email id

    When I click on forget password link
    Then I redirect forget password page
    And Click on reset button
    Then I see validation message

  Scenario: email id and password validation

    When Enter email id with invalid domain name as shivanit@vp.com
    And Enter valid password
    And Click on login button
    Then I see error message

    When Enter email id without dot as shivani@gmailcom
    And Enter valid password
    And Click on login button
    Then Show error Email is an invalid email.

    When Enter email id as shivani@gmail.com
    When Enter password with space
    And Click on login button
    Then I see error message

    When Enter email id without @ as shivani123
    And Enter valid password
    And Click on login button
    Then I see error message

