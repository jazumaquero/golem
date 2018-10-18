from math import fabs

FORWARD = 'forward'
BACKWARD = 'backward'
LEFT = 'left'
RIGHT = 'right'
STOP = 'stop'


class DifferentialMotorAdapter(object):
    def __init__(self, robot):
        self.robot = robot

    def move(self, vx, vy):
        if vx == vy == 0:
            self.robot.stop()
        elif vy == 0:
            self.robot.left(speed=fabs(vx)) if vx < 0 else self.robot.right(speed=vx)
        else:
            kwargs = {'speed': fabs(vy), 'curve_left': fabs(vx) if vx < 0 else 0, 'curve_right': vx if vx > 0 else 0}
            self.robot.backward(**kwargs) if vy < 0 else self.robot.forward(**kwargs)
