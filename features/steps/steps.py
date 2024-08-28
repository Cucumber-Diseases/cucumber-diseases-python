from behave import *

from customer import CustomerService
from datetime import date, datetime
from assertpy import assert_that

@given(u'the customer first name is "(?P<name>.*)"')
def step_impl(context, name):
    context.first_name = name


@given(u'the customer last name is "(?P<name>.*)"')
def step_impl(context, name):
    context.last_name = name


@given("the customer's birthday is (?P<d>.*)")
def the_customers_birthday_is(context, d):
    context.birthday = datetime.strptime(d, "%Y/%m/%d").date()


@when(u'the customer is created')
def step_impl(context):
    try:
        context.service.add_customer(context.first_name, context.last_name, context.default_birthday)
    except ValueError as e:
        context.error = e


@then(u'the customer creation should be successful')
def step_impl(context):
    pass


@given(u'there are no customers')
def step_impl(context):
    pass


@given(u'the customer name is (?P<first_name>.*?) (?P<last_name>.*?)')
def step_impl(context, first_name, last_name):
    context.first_name = first_name
    context.last_name = last_name


@when(u'all customers are searched')
def step_impl(context):
    context.count = len(context.service.search_customers())


@then(u'the number of customers found is (?P<n>\d+)')
def step_impl(context, n):
   assert_that(context.count).is_equal_to(int(n))


@when(u'an invalid customer is created')
def step_impl(context):
    try:
        context.service.add_customer(context.first_name, context.last_name, context.default_birthday)
    except ValueError as e:
        context.error = e


@then(u'the customer creation should fail')
def step_impl(context):
    assert_that(context).contains("error")
    assert_that(str(context.error)).is_equal_to("Mandatory name parameter is missing")



@given(u'the second customer is (?P<first_name>.*?) (?P<last_name>.*?)')
def step_impl(context, first_name, last_name):
    context.second_first_name = first_name
    context.second_last_name = last_name


@when(u'the second customer is created')
def step_impl(context):
    pass


@then(u'the second customer can be found')
def step_impl(context):
    context.service.add_customer(context.second_first_name, context.second_last_name, context.default_birthday)
    customer = context.service.search_customers(context.second_first_name, context.second_last_name)

    assert_that(customer).is_not_none()

@then(u'the second customer creation should fail')
def step_impl(context):
    caught = None
    try:
        context.service.add_customer(context.second_first_name, context.second_last_name, context.default_birthday)
    except ValueError as e:
        caught = e

    assert_that(caught).is_not_none()
    assert_that(str(caught)).is_equal_to("Customer already exists")


@given(u'there is a customer')
def step_impl(context):
        table = context.table
        context.service.add_customer(table.headings[0], table.headings[1], context.default_birthday)


@then(u'the customer Sabine Mustermann can be found')
def step_impl(context):
    customer = context.service.search_customer("Sabine", "Mustermann")
    assert_that(customer.first_name).is_equal_to("Sabine")
    assert_that(customer.last_name).is_equal_to("Mustermann")


@given(u'the customer is created')
def step_impl(context):
    try:
        context.service.add_customer(context.first_name, context.last_name, context.default_birthday)
    except ValueError as e:
        context.error = e


@when(u'the customer Sabine Mustermann is searched')
def step_impl(context):
    context.count = len(context.service.search_customers("Sabine", "Mustermann"))


@given(u'there are some customers')
def step_impl(context):
    for row in context.table.rows:
        context.service.add_customer(row["firstname"], row["lastname"], context.default_birthday)
