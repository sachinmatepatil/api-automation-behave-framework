@data-driven @booking
Feature: To create booking Data drive testing
  Scenario Outline: Create booking with multiple datasets
    Give the API base URL is set
    When I send a post request to "/booking" using dataset "<dataset>"
    Then the response status code should be <status_code>

    Examples:
      | dataset | status_code |
      |0        | 200         |
      |1        | 400         |
