# Created by Galac at 08/09/2024
Feature: Tests for Target Search functionality

  Scenario: User can see the cart icon
    Given Open target.com
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown


  Scenario: User can go on sigh in page
    Given Open target.com
    When Click Sign In
    And From right side navigation menu, click Sign In
    Then Verify Sign In form opened