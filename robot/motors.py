from math import fabs

FORWARD = 'forward'
BACKWARD = 'backward'
LEFT = 'left'
RIGHT = 'right'
STOP = 'stop'


class DifferentialMotorController(object):
    def __init__(self, robot):
        self.robot = robot

    def move(self, vx, vy):
        def partial():
            if vx == vy == 0:
                action = STOP
                attributes = {}
            elif vy == 0:
                action = LEFT if vx < 0 else RIGHT
                attributes = {'speed': fabs(vx)}
            else:
                action = BACKWARD if vy < 0 else FORWARD
                attributes = {'speed': fabs(vy), 'curve_left': fabs(vx) if vx < 0 else 0,
                              'curve_right': vx if vx > 0 else 0}

            return action, attributes

        action, attributes = partial()
        action_method = self.robot.getattribute(action)()
        action_method(**attributes)
