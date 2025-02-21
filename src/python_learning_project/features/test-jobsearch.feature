Feature: Search jobs with technical skills
    #Background:
    #  Given the user is logged in
    #  And the user navigates to the job search link

  Scenario Outline: Verify skill matched jobs in the search result when <scenarioName>
    Given test data <testData> file is used
    When the user visited job serve website
    When the user search for a job by technical skills details
    Then the user is on Job results page

    Examples:
      | scenarioName                          | testData                                 |
      | the user searches by technical skills | fixtures/testData/searches/job-search-with-technical-skill.json |
