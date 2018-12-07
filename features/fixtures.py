from behave import fixture

from robot.actuators import STOP, RIGHT, BACKWARD, FORWARD, LEFT


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
        self.direction = STOP


class MockedServo(object):
    def __init__(self):
        self.angle = None


@fixture
def robot(context, **kwargs):
    context.robot = MockedRobot()


@fixture
def pan_tilt(context, **kwargs):
    context.pan_servo = MockedServo()
    context.tilt_servo = MockedServo()
