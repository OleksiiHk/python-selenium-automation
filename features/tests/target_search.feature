# Created by Galac at 08/09/2024
Feature: Tests for Target Search functionality

  Scenario: User can go on sigh in page
    Given Open target.com
    When Click Sign In
    And From right side navigation menu, click Sign In
    Then Verify Sign In form opened


  Scenario: User can search for a tea
    Given Open target.com
    When Search for a coffee
    Then Verify that correct search result shows for coffee
    Then Verify product coffee in URL


  Scenario: User can search for a product
    Given Open target.com
    When Search for a tea
    Then Verify that correct search result shows for tea


  Scenario Outline: User can search for product
    Given Open target.com
    When Search for a <search_word>
    Then Verify that correct search result shows for <search_result>
    Examples:
    |search_word| search_result |
    |milk       | milk          |
    |apples     | apples        |
    |bread      | bread         |
    |milk       | milk          |
    |eggs       | eggs          |
    |chicken    | chicken       |
    |rice       | rice          |
    |cheese     | cheese        |
    |tomatoes   | tomatoes      |
    |potatoes   | potatoes      |
    |pasta      | pasta         |

  Scenario: User can add a product to the cart
    Given Open target.com
    When Search for a coffee
    And Click on Add to Cart button
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item

  Scenario: Verify that user can see product names and images
    Given Open target.com
    When Search for a AirPods (3rd Generation)
    Then Verify that every product has a name and an image