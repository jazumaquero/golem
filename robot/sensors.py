from robot.core import Sensor


class UltrasonicDistanceSensor(Sensor):
    def __init__(self, distance_sensor):
        self.distance_sensor = distance_sensor

    def measure(self):
        return self.distance_sensor.distance
