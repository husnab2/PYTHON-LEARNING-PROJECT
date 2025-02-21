from pages.SearchPage import SearchPage
from behave import *

@given('test data {testData} file is used')
def user_test_data_file_is_used(context, testData):
  context.jobsearch_page = SearchPage(context.driver, testData)
  

@when('the user visited job serve website')
def user_visited_job_serve_url(context):
  context.jobsearch_page.navigate_jobsearch_url()

@when('the user search for a job by technical skills details')
def user_search_for_a_job_by_techical_skills(context):
  context.jobsearch_page.populate_form()

@then('the user is on Job results page')
def user_is_on_job_results_page(context):
  context.jobsearch_page.verify_search_result()

