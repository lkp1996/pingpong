Feature: As a user, I want to see the list of all the games of a specific player so that I can see more easily the games of a specific player

    Scenario: Select a player in the dropdown list
        Given I am on the Scoreboard page
        When I select <the_player>
        Then I see all the games played by <the_player>
