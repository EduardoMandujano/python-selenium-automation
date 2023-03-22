# Created by Eduardo at 3/20/2023
Feature:  Homework 8
  Practice for Dropdown Menus, Hovering and Action Chains.

  Scenario: While on a product from closing category, user hovers on New Arrivals and sees the deals
    Given Open Sample Closing Category Product Page
    When Hover over New Arrivals option
    Then Verify that user can see the New Arrivals deals

  Scenario: User can select and search in a specific Amazon Department
    Given Open Amazon page
    When Select department by alias luxury
    When Input text Prada
    When Click on magnifying glass icon
    Then Verify that luxury Department is selected