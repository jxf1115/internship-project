# Created by jfernandez at 8/27/23
Feature: Amazon Signin and Cart Test scenarios for Lesson 3
  # Enter feature description here

  Scenario: Verify that clicking Orders takes to signin
    Given Open Amazon page
    When Click Orders
    Then Verify sign in page opened



  Scenario: Verify that clicking Cart Icon takes to empty Cart
    Given Open Amazon page
    When Click Cart Icon
    Then Cart is open