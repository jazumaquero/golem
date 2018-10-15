from paho.mqtt import publish, subscribe


class mqtt_publish(object):
    def __init__(self, host, port, topic):
        self.host = host
        self.port = port
        self.topic = topic

    def __call__(self, func):
        def wrapped(*args, **kwargs):
            message = func(*args, **kwargs)
            publish.single(hostname=self.host, port=self.port, topic=self.topic, payload=message)

        return wrapped


def mqtt_subscribe(host, port, topic, keepalive, on_message):
    subscribe.callback(on_message, topic, hostname=host, port=port, keepalive=keepalive)
