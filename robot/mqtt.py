from paho.mqtt import publish, subscribe


class MqttOutputAdapter(object):
    def __init__(self, config):
        self.config = config

    def __call__(self, func):
        def wrapped(*args, **kwargs):
            kwargs = {
                'hostname': self.config.hostname,
                'port': self.config.port,
                'topic': self.config.topic,
                'qos': self.config.qos,
                'payload': func(*args, **kwargs)
            }
            publish.single(**kwargs)

        return wrapped


class MqttInputAdapter(object):
    def __init__(self, config):
        self.config = config

    def __call__(self, func):
        kwargs = {
            'hostname': self.config.hostname,
            'port': self.config.port,
            'qos': self.config.qos,
            'keepalive': self.config.keepalive,
            'topics': self.config.topics,
            'callback': func
        }
        subscribe.callback(**kwargs)
