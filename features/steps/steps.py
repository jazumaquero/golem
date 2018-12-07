from behave import given, when, then
from nose.tools import assert_equal, assert_is_none

from robot.actuators import DifferentialMotorActuator, STOP, RIGHT, BACKWARD, FORWARD, LEFT

MISSING = '-'


def assert_robot_attribute(robot, attribute, value):
    if not robot.direction == STOP:
        if value and not value == MISSING:
            assert_equal(float(value), robot.attributes.get(attribute))
        else:
            assert_is_none(robot.attributes.get(attribute))


@given(u'robot vx equal {value}')
def step_impl(context, value):
    context.vx = float(value)


@given(u'robot vy equal {value}')
def step_impl(context, value):
    context.vy = float(value)


@when(u'do robot movement')
def step_impl(context):
    #context.robot = MockedRobot()
    context.controller = DifferentialMotorActuator(robot=context.robot)
    context.controller.action(vx=context.vx, vy=context.vy)


@then(u'robot direction {direction}')
def step_impl(context, direction):
    assert_equal(direction.lower(), context.robot.direction)


@then(u'robot speed is {value}')
def step_impl(context, value):
    assert_robot_attribute(context.robot, 'speed', value)


@then(u'robot curve left is {value}')
def step_impl(context, value):
    assert_robot_attribute(context.robot, 'curve_left', value)


@then(u'robot curve right is {value}')
def step_impl(context, value):
    assert_robot_attribute(context.robot, 'curve_right', value)
