# Created by jfernandez at 9/23/23
Feature: # Verify BestSellers links and Cart Test scenarios for Lesson 4
  # Enter feature description here


  Scenario: Verify that navigating to Best Sellers page contains 5 links
    Given Open Amazon page
    When Click Best Sellers
    Then Verify 5 bestseller links on page
