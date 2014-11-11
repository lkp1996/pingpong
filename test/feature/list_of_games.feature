Feature: As a user, I want to see a list of games
    so that I can see all the games played

    Scenario: Opening "Scoreboard" page
        Given I am on the project hompage
        When I click on the "Scoreboard" link in the menu
        Then I am redirected to a page with a list of all the games played and a search dropdown list

    Scenario: No games played
        Given I am on the Scoreboard page
        When the games table in the database is empty
        Then I see a message says "No games"
