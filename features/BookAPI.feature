# Created by user at 6/19/2024
Feature: Verify if Books are added and deleted using Library API
  # Enter feature description here
  @library
  Scenario: Verify AddBook API functionality
    Given the book details which needs to be added to library
    When we execute the AddBook PostAPI method
    Then book is successfully added
    And status code of response should be 200

  @library
  Scenario Outline: Verify AddBook API functionality
    Given the book details with <isbn> and <aisle>
    When we execute the AddBook PostAPI method
    Then book is successfully added
    Examples:
      | isbn  | aisle |
      | mdkee | 2838  |
      | jofgf | 9649  |



    # Enter steps here