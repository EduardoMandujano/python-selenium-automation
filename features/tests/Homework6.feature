# Created by Eduardo Mandujano at 3/5/2023
Feature:  Homework 6
  Multiple Window Handling Test Case

  Scenario: User can open and close Amazon Privacy Notice
    Given Open Amazon Terms and Conditions page
    When Store original windows
    And Click on Amazon Privacy Notice link
    And Switch to the newly opened window
    Then Verify Amazon Privacy Notice page is opened
    And User can close new window
    And Switch back to original window