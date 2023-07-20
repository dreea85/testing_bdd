Feature: Test the login module

  @customer
  Scenario: Test unregistrered email for "No customer account found" when the user tries to log in with an unregistred email
    Given I am on the login page
    When I introduce an unregistred email in the email field
    And I introduce the password
    And I click on the login button
    Then the main error message is displayed
    And the error message contains "No customer account found"

  @param
  Scenario: Test unregistrered email for "No customer account found" when the user tries to log in with an unregistred email
    Given I am on the login page
    When I introduce "ceva@gmail.com" in the email field
    And I introduce the password
    And I click on the login button
    Then the main error message is displayed
    And the error message contains "No customer account found"

  Scenario: Check that "Wrong email" is displayed when the user enters an empty email address
    Given I am on the login page
    When I introduce an invalid email in the email field
    And I click on the login button
    Then the email error message is displayed
    And the error message contains "Wrong email"