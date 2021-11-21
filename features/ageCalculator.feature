Feature: Retirement Age Calculator
  This is a calculator that will determine when a person can retire,
  The calculator will output their retirement age and months,
  The calculator will also output their retirement date year and month.

  Scenario: Determine Retirement Age
    Given an input request
    When the user submits 1998 for the birth year and 2 for the birth month
    Then  the retirement age will be 67 years and 2 months


  Scenario: Determine Retirement Date
      Given an input request
      When the user submits 1998 for the birth year and 2 for the birth month
      Then the retirement date will be February 2065
