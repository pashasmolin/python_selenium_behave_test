Feature: Member Tests

  Scenario: Livongo Login
    Given I navigate to the Livongo Login page
    When I login with username "valid_login" and password "valid_password"
    Then I am taken to the Livongo Dashboard page
