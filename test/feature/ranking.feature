Feature: As an user, I want to see the ranking of every player
    so that I can see my rank

    Scenario: Opening "Ranking" page
        Given I am on the project  homepage
        When I click on the "Ranking" link in the menu
        Then I am redirected to a page with a list of player order by their rank

    Scenario: No player in the system
        Given I am on the Ranking page
        When the players table in the database is empty
        Then I see a message says "Ranking empty"
