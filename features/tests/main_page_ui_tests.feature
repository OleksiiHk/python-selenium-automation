Feature: Tests for main page UI

  Scenario: Verify header in shown
    Given Open target.com
    Then Verify header is shown

  Scenario: Verify header has correct amount links
    Given Open target.com
    Then Verify header is shown
    And Verify header has 6 links