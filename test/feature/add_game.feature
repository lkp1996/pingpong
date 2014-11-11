Feature: As a user, I want to input a game result so that this game is saved

    Scenario: Opening "Add Game" page
        Given I am on the project homepage
        When I click on the "Add Game" link in the menu
        Then I am redirected to a page with two dropdown menus for players, two score inputs, one save button and a name input to create a player

    Scenario: Adding a game with no players
        Given I am on the add game page
        When I increase score one to <number_one>
        And I increase score two to <number_two>
        And I click on the save button
        Then I am redirected to the same page and an error says "All fields are required"

    Scenario: Adding a game with one player
        Given I am on the add game page
        When I select player one value or player two value but not both
        And I increase score one to <number_one>
        And I increase score two to <number_two>
        And I click on the save button
        Then I am redirected to the same page and an error says "All fields are required"


    Scenario: Adding a game with different players and same score
        Given I am on the add game page
        When I select player one value <player_one>
        And I select player two value  <player_two>
        And I increase score one to <number>
        And I increase score two to <number>
        And I click on the save button
        Then I am redirected to the same page and an error says "Scores need to be different"


    Scenario: Adding a game with same players and different score
        Given I am on the add game page
        When I select player one value to <player>
        And I select player two value  to <player>
        And I increase score one to <number_one>
        And I increase score two to <number_two>
        And I click on the save button
        Then I am redirected to the same page and an error says "Players need to be different"


    Scenario: Adding a game two different players and scores
        Given I am on the add game page
        When I select player one value to <player_one>
        And I select player two value  to <player_two>
        And I increase score one to <number_one>
        And I increase score two to <number_two>
        And I click on the save button
        Then I am redirected to the same page and a message says "Game added"
