from behave import use_fixture

from features.fixtures import robot, pan_tilt


def before_tag(context, tag):
    if tag == 'robot':
        use_fixture(robot, context)
    elif tag == 'pan_tilt':
        use_fixture(pan_tilt, context)
