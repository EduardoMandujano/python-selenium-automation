# Created by Eduardo Mandujano at 2/28/2023
Feature: Homework 5
  Test Case with a For Loop and Test Case to verify product name and image

  Scenario: User can click through the entire color selection of a product
    Given Navigate to Amazon B07BJKRR25 Mens Jeans Page
    Then Verify that user can click and select any color

    # This scenario does NOT work yet
    # Scenario: User sees that products on Amazon search results have a product name and image
      # Given Open Amazon page
      # When Input kettlebells into the search field
      # And Click on magnifying glass icon
      # Then Verify that search results have a product name and image
