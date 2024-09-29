# Created by Galac at 09/09/2024
Feature: Cart Tests
  # Enter feature description here


  Scenario: User can see the cart icon
    Given Open target.com
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown



