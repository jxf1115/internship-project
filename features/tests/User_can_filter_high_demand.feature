# Created by jfernandez at 10/12/23
Feature: Tests for Reelly Main Page UI


  Scenario: Verify that user can filter by sales status High Demand
    Given Open Reelly page
    When Login
    When Click on Filters
    When Click on High Demand
    When Wait for 4 sec
    Then Verify each product contains High Demand tag


