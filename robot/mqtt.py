from paho.mqtt import publish, subscribe

from .core import Publisher, Subscriber


class MqttPublisher(Publisher):
    def __init__(self, config):
        self.config = config

    def publish(self, message):
        publish.single(**{**self.config, **{'payload': message}})


class MqttSubscriber(Subscriber):
    def __init__(self, config):
        self.config = config

    def subscribe(self, func):
        def partial(client, userdata, message):
            func(message.payload)

        subscribe.callback(**{**self.config, **{'callback': partial}})
