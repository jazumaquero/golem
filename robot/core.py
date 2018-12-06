from json import dumps, loads
from time import sleep


class Serializer(object):
    def serialize(self, obj):
        return dumps(obj)


class Deserializer(object):
    def deserialize(self, message):
        return loads(message)


class Publisher(object):
    def publish(self, message):
        raise NotImplementedError


class Subscriber(object):
    def subscribe(self, func):
        raise NotImplementedError


class Sensor(object):
    def measure(self):
        raise NotImplementedError


class Actuator(object):
    def action(self, *args, **kwargs):
        raise NotImplementedError


class SensorSource(object):
    def __init__(self, publisher, serializer, sensor, period=None):
        self.publisher = publisher
        self.serializer = serializer
        self.sensor = sensor
        self.period = period

    def run(self):
        while True:
            measure = self.sensor.measure()
            message = self.serializer.serialize(measure)
            self.publisher.publish(message)
            if self.period:
                sleep(self.period)


class ActuatorSink(object):
    def __init__(self, subscriber, deserializer, actuator):
        self.subscriber = subscriber
        self.deserializer = deserializer
        self.actuator = actuator

    def run(self):
        def callback(message):
            obj = self.deserializer.deserialize(message)
            self.actuator(obj)

        self.subscriber.subscribe(callback)
