@booking @create @positive
Feature: To create booking using BookingAPI
    Scenario: Create booking with valid details
      Given the API base URL is set
        When I send a POST request to "/booking" with the following details:
          | firstname | lastname | totalprice | depositpaid | checkin     | checkout    | additionalneeds |
          | John      | Doe      | 150        | true        | 2023-10-01  | 2023-10-10  | Breakfast       |
        Then the response status code should be 200
        And the response should contain the booking id
        And the firstname should be "John"
        And the lastname should be "Doe"



    Scenario: Create booking with invalid details
      Given the API base URL is set
        When I send a POST request to "/booking" with the following details:
          | firstname | lastname | totalprice | depositpaid | checkin     | checkout    | additionalneeds |
          |           |          | -50        | maybe       | 2023-10-10  | 2023-10-01  |                 |
        Then the response status code should be 400
        And the response should contain an error message indicating invalid input

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
