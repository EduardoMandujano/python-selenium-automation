# Created by Eduardo at 2/21/2023
Feature: Homework 4
  More Behave Practice

  Scenario: If user opens Best Sellers page 5 links are present
    Given Open Amazon page
    When Click on Best Sellers option
    Then User sees five links present


  Scenario: If user adds product to cart product is present in cart
    Given Open Amazon page
    When Input kettlebells into the search field
    And Click on magnifying glass icon
    And Click on first kettlebells displayed
    And Add kettlebells to cart
    Then Verify that kettlebells were added to cart


  Scenario: User sees that select Customer Service page UI elements are present
    Given Open Amazon page
    When Click on Customer Service option
    Then Verify the presence of Welcome to Amazon Customer Service header
    Then Verify the presence of the Customer Service Clickable Table
    Then Verify the presence of the Search our help library header
    Then Verify the presence of the Search our help library input field
    Then Verify the presence of the All help topics header
    Then Verify the presence of the Recommended Topics list

