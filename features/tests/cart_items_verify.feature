# Created by jfernandez at 9/23/23
Feature: Amazon Cart Test scenario for Lesson 4
  # Enter feature description here

  Scenario: Verify that clicking Cart Icon takes to empty Cart
    Given Open Amazon page
    When Search for table
    When Click on product
    When Click Add to Cart
    Then Verify Cart has product
