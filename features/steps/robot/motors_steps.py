from behave import given, when, then

from robot.motors import *


class MockedRobot(object):
    def __init__(self):
        self.direction = None
        self.attributes = None

    def forward(self, **kwargs):
        self.direction = FORWARD
        self.attributes = dict(kwargs)

    def backward(self, **kwargs):
        self.direction = BACKWARD
        self.attributes = dict(kwargs)

    def left(self, **kwargs):
        self.direction = LEFT
        self.attributes = dict(kwargs)

    def right(self, **kwargs):
        self.direction = RIGHT
        self.attributes = dict(kwargs)

    def stop(self):
        self.directions = STOP


@given(u'vx equal "{value}"')
def step_impl(context, value):
    context.vx = float(value)


@given(u'vy equal "{value}"')
def step_impl(context, value):
    context.vy = float(value)


@when(u'do robot movement')
def step_impl(context):
    context.robot = MockedRobot
    context.controller = DifferentialMotorController(robot=context.robot)
    context.controller.move(vx=context.vx, vy=context.vy)


@then(u'robot is stopped')
def step_impl(context):
    assert context.robot.direction == STOP


@then(u'robot moves "{direction}" with speed "{speed}" and curve left "{curve_left}" and curve right "{curve_right}"')
def step_impl(context, direction, speed, curve_left, curve_right):
    assert context.robot.direction == direction
    assert context.robot.attributes['speed'] == float(speed)
    assert context.robot.attributes['curve_left'] == float(curve_left)
    assert context.robot.attributes['curve_right'] == float(curve_right)


@then(u'robot moves "{direction}" with speed "{speed}"')
def step_impl(context, direction, speed):
    assert context.robot.direction == direction
    assert context.robot.attributes['speed'] == float(speed)
