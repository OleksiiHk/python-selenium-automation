# Created by Galac at 09/09/2024
Feature: Cart Tests
  # Enter feature description here

  Scenario: User can go on sigh in page
    Given Open target.com
    When Click Sign In
    And From right side navigation menu, click Sign In
    Then Verify Sign In form opened



