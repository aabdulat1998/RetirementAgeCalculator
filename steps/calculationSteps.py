from behave import given, when, then
from RetirementCalculator import retirement_calculator


@given(u'an input request')
def step_impl(context):
    print(u'STEP: Given an input request')
    pass


@when(u'the user submits "{inp1}" for the birth year and {inp2} for the birth month')
def step_impl(context, inp1, inp2):
    print(u'STEP: When the user submits "{}" for the birth year and "{}" for the birth month'.format(inp1, inp2))
    context.result = retirement_calculator(inp2, inp1)


@then(u'the retirement date will be "{out}"')
def step_impl(context, out):
    print(u'STEP: Then the retirement date will be "{}"'.format(out))
    assert context.result == str(out), 'Expected {}, got {}'.format(out, context.result)
