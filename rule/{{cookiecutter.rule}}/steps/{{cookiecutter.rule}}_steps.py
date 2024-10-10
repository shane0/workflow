@given(u'you are ready')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given you are ready')


@when(u'inputs do this')
def step_impl(context):
    raise NotImplementedError(u'STEP: When inputs do this')


@when(u'algorithms do that')
def step_impl(context):
    raise NotImplementedError(u'STEP: When algorithms do that')


@then(u'this output appears')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then this output appears')