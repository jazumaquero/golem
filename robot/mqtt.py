import json

import yaml
from paho.mqtt import publish, subscribe


class MqttConfig(object):
    def __init__(self, path='resources/config.yml', file_format='yml'):
        with open(path) as file:
            if file_format.lower() == 'yml':
                self.config = yaml.load(file)['mqtt']
            if file_format.lower() == 'json':
                self.config = json.load(file)['mqtt']
            else:
                raise NotImplementedError('Not supported configuration format')


class MqttOutputAdapter(MqttConfig):
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


class MqttInputAdapter(MqttConfig):
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
