Feature: Tests for main page UI

  Scenario: Verify header in shown
    Given Open target.com
    Then Verify header is shown


  Scenario: Verify header has correct amount links
    Given Open target.com
    Then Verify header is shown
    And Verify header has 6 links


  Scenario: Verify benefit cells are displayed correctly
    Given Open the Target Circle page
    Then Verify that there are 10 benefit cells


  Scenario: Verify UI elements on Target Help page
    Given Open https://help.target.com/help
    Then Verify "Target Help" header is displayed
    And Verify "search help" input field and "track an order" button are displayed
    And Verify header has 7 buttons
    And Verify "contact us" and "holiday help" sections are displayed
    And Verify "Browse all Help pages" text is displayed

