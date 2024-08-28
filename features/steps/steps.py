from assertpy import assert_that
from behave import *


@then(u'the customer creation should be successful')
def step_impl(context):
    assert_that(context.error).is_none()


@given(u'there are no customers')
def step_impl(context):
    pass


@when(u'all customers are searched')
def step_impl(context):
    context.count = len(context.service.search_customers())


@then(u'the number of customers found is (?P<n>\d+)')
def step_impl(context, n):
   assert_that(context.count).is_equal_to(int(n))


@then(u'the customer creation should fail with "(?P<error_message>.*?)"')
def step_impl(context, error_message):
    assert_that(context).contains("error")
    assert_that(str(context.error)).is_equal_to(error_message)


@then(u'the customer (?P<first_name>.*?) (?P<last_name>.*?) can be found')
def step_impl(context, first_name, last_name):
    customer = context.service.search_customer(first_name, last_name)
    assert_that(customer.first_name).is_equal_to(first_name)
    assert_that(customer.last_name).is_equal_to(last_name)


@when("the customer (?P<first_name>.*?) (?P<last_name>.*?) is created")
@when("the second customer (?P<first_name>.*?) (?P<last_name>.*?) is created")
@when("an invalid customer (?P<first_name>.*?) (?P<last_name>.*?) is created")
def step_impl(context, first_name, last_name):
    try:
        context.service.add_customer(first_name, last_name, context.default_birthday)
    except ValueError as e:
        context.error = e


@when(u'the customer (?P<first_name>.*?) (?P<last_name>.*?) is searched')
def step_impl(context, first_name, last_name):
    context.count = len(context.service.search_customers(first_name, last_name))


@given(u'there is a customer')
@given(u'there are some customers')
def step_impl(context):
    for row in context.table.rows:
        context.service.add_customer(row["firstname"], row["lastname"], context.default_birthday)

