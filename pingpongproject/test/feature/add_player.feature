Feature: As a user, I want to add a player if he’s not in the list so that I can input a game with my created player

    Scenario: Adding an empty name player
        Given I am on the add game page
        When I click on the "Add the player" button
        Then I am redirected to the same page and an error says "The field 'Name' is required"

    Scenario: Adding a player with a valid name
        Given I am on the add game page
        When I write <player_name> in the text input
        And I click on the "Add the player" button
        Then I am redirected to the same page with a message says "Player added" and the name of the player should be in the two dropdown lists above

    Scenario: Adding an existing player
        Given I am on the add game page
        When I write an existing name player
        And I click on the "Add the player" button
        Then I am redirected to the same page and an error says "This player already exists"

    Scenario: Adding an player with a longer than 50 characters name
        Given I am on the add game page
        When I write a player name with more than 50 characters
        And I click on the "Add the player" button
        Then I am redirected to the same page and an error says "The name is too long (max. 50 characters)"
