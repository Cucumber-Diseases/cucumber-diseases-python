Feature: Customer

    Scenario: Should successfully create new customer
      When the customer Max Mustermann is created
      Then the customer creation should be successful

    Scenario: Should find newly created customer
      When the customer Rose Smith is created
      Then the customer Rose Smith can be found

    Scenario Outline: Cannot create customer without first or lastname
      When an invalid customer <firstname> <lastname> is created
      Then the customer creation should fail with "Mandatory name parameter is missing"
      Examples:
        | description    | firstname | lastname   |
        | only firstname | Max       |            |
        | just lastname  |           | Mustermann |
        | neither nor    |           |            |

    Scenario: Should be able to create two customer with different names
      Given there is a customer
        | firstname | lastname   |
        | Max       | Mustermann |
      When the second customer Sabine Mustermann is created
      Then the customer Sabine Mustermann can be found

    Scenario: Cannot create two customer with the same name
      Given there is a customer
        | firstname | lastname   |
        | Max       | Mustermann |
        | Sabine    | Mustermann |
      When the customer Sabine Mustermann is created
      Then the customer creation should fail with "Customer already exists"

    Scenario: Should find an existing customer
      Given there is a customer
        | firstname | lastname |
        | Sabine | Mustermann  |
      Then the customer Sabine Mustermann can be found

    Scenario: Should find customers by name
      Given there is a customer
        | firstname | lastname |
        | Sabine | Mustermann  |
      When the customer Sabine Mustermann is searched
      Then the number of customers found is 1

    Scenario: Cannot find customer that does not exist
      Given there are no customers
      When all customers are searched
      Then the number of customers found is 0

    Scenario: Should find multiple customers
      Given there are some customers
        | firstname | lastname   |
        | Max       | Mustermann |
        | Sabine    | Mustermann |
        | Horst     | Mustermann |
      When all customers are searched
      Then the number of customers found is 3