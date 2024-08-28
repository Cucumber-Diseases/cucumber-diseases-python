from datetime import date

from behave import use_step_matcher

from customer import CustomerService


def before_scenario(context, scenario):
    context.service = CustomerService()
    context.default_birthday = date(1995, 1, 1)
    context.error = None

use_step_matcher("re")