@users @negative
Feature: User lookup(negative)
  when we use user API
  we want to have a clear error message for invalid users
  so that we can handle 404 cases safely

    Scenario Outline: GET /booking/<id> returns 404 for invalid booking
      Given the API base URL is set
      When I send a GET request to "booking/<id>"
      Then the response status code should be 404
      And the response should contain an error message or be empty
      Examples:
        | id |
        | 99999|
        | -12 |
        | asd |