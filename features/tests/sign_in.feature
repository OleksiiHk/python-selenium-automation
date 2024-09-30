# Created by Galac at 29/09/2024
Feature: Sign in page test

  Scenario: Log in to target.com
    Given Open target.com
    When Click Sign In
    And From right side navigation menu, click Sign In
    And Input email and password on SignIn page
    And Click "Sign in with password"
    Then Verify user is logged in
