# Created by Galac at 08/09/2024
Feature: Tests for Target Search functionality

  Scenario: User can see the cart icon
    Given Open target.com
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown


  Scenario: User can search for a product
    Given Open target.com
    When Search for a coffee
    Then Verify that correct search result shows for coffee


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
    When Search for coffee
    And Click on the product in the search results
    And Click "Add to Cart" from the side menu
    And Open cart page
    Then Verify cart has 1 item

