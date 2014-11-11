Feature: As a user, I want to navigate to a home page with a welcome message
    so that I know what this website is about

    Scenario: Root Page
        When I go to the root of the website
        Then I see the homepage with a welcome message
        And the result of every game played today

    Scenario: Opening "Home" page
        Given I am on any page
        When I click on the "Home" link in the menu
        Then I am redirected to the homepage
