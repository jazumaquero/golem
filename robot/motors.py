from math import fabs

from robot.core import Actuator

FORWARD = 'forward'
BACKWARD = 'backward'
LEFT = 'left'
RIGHT = 'right'
STOP = 'stop'


class DifferentialMotorActuator(Actuator):
    def __init__(self, robot):
        self.robot = robot

    def action(self, vx, vy):
        if vx == vy == 0:
            self.robot.stop()
        elif vy == 0:
            self.robot.left(speed=fabs(vx)) if vx < 0 else self.robot.right(speed=vx)
        else:
            kwargs = {'speed': fabs(vy), 'curve_left': fabs(vx) if vx < 0 else 0,
                      'curve_right': vx if vx > 0 else 0}
            self.robot.backward(**kwargs) if vy < 0 else self.robot.forward(**kwargs)


class PanTiltMotorActuator(Actuator):
    def __init__(self, pan_servo, tilt_servo):
        self.pan_servo = pan_servo
        self.tilt_servo = tilt_servo

    def action(self, pan, tilt):
        self.pan_servo.angle = pan
        self.tilt_servo.angle = tilt
