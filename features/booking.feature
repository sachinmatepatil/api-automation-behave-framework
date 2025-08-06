Feature: Users API testing

  Scenario: Verify GET /booking API
    Given the API base URL is set
    When I send a GET request to "/booking"
    Then the response status code should be 200