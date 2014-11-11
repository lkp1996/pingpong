Feature: As a user, I want to see the result of every game played today so that I have a review of what happened today

    Scenario: No game played the current day
        Given I am on the Homepage
        When there is not any game played during the current day
        Then I see a message says "No game played today"
