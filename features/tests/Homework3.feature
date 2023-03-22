# Created by Eduardo at 2/17/2023
Feature: Homework 3
  BDD Practice Re-written with Page Object Pattern for HW7

  Scenario: Logged-out user sees Sign In when clicking on Returns and Orders
    Given Open Amazon page
    When Click on Orders
    Then Sign-in header is visible
    Then Input Field is Present

   Scenario: Logged-out user clicks on Cart Icon and sees Amazon Cart Empty
     Given Open Amazon page
     When Click on Cart icon
     Then Cart is empty