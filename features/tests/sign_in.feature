# Created by Galac at 29/09/2024
Feature: Sign in page test

  Scenario: Log in to target.com
    Given Open target.com
    When Click Sign In
    And From right side navigation menu, click Sign In
    And Input email and password on SignIn page
    And Click "Sign in with password"
    Then Verify user is logged in


  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open target.com
    When Click Sign In
    And From right side navigation menu, click Sign In
    And Store original window
    And Click on Target terms and conditions link
    And Switch to new window
    Then Verify Terms and Conditions page is opened
    And Close current page
    And Return to original window