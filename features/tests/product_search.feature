# Created by Svetlana at 4/4/19
  #Edited by Eduardo on 02/01/2023
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Google page
    When Input Coffee into search field
    And Click on search icon
    Then Product results for Coffee are shown
