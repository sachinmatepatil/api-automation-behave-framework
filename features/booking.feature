Feature: Users API testing

  Scenario: Verify GET /booking API
    Given the API base URL is set
    When I send a GET request to "/booking"
    Then the response status code should be 200
    And the response should be valid


  Scenario Outline: Verify GET /booking/<id> API
    Given the API base URL is set
    When I send a GET request to "booking/<id>"
    Then the response status code should be 200
    Examples:
    |id   |
    |2742 |


  Scenario: Verify GET /booking/<id> from external JSON
    Given the API base URL is set
    When I send a GET request to booking from "test_data/b_id.json"
    Then the response status code should be 200

