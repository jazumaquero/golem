from math import atan2, pi, sqrt, pow
from time import time


class Mpu6050ImuAdapter(object):
    INIT_REGISTERS = [
        {'register': 'power_management', 'address': 0x6B, 'value': 1},
        {'register': 'sample_rate_divider', 'address': 0x19, 'value': 7},
        {'register': 'config', 'address': 0x1A, 'value': 0},
        {'register': 'gyro_config', 'address': 0x1B, 'value': 24},
        {'register': 'interruption_enable', 'address': 0x38, 'value': 1}
    ]
    ACCELERATION_REGISTERS = {'ax': 0x3B, 'ay': 0x3D, 'az': 0x3F}
    GYRO_REGISTERS = {'gx': 0x43, 'gy': 0x45, 'gz': 0x47}
    ACCELERATION_SCALE_FACTOR = 16384.0
    GYRO_SCALE_FACTOR = 131.0

    def __init__(self, bus, device_address=0x68, has_complementary_filter=True, alpha=0.98):
        def set_register(address, value):
            self.bus.write_byte_data(self.device_address, address, value)

        self.bus = bus
        self.device_address = device_address
        self.has_complementary_filter = has_complementary_filter
        self.alpha = alpha
        self.beta = 1 - alpha
        self.t_minus_one = time()
        [set_register(register['address'], register['value']) for register in self.INIT_REGISTERS]

    def measure(self):
        def word_to_int(high, low):
            value = ((high << 8) | low)
            return value if value <= 32768 else value - 65536

        def read_raw_data(register):
            high = self.bus.read_byte_data(self.device_address, register)
            low = self.bus.read_byte_data(self.device_address, register + 1)
            return word_to_int(high, low)

        def read_acceleration(register):
            return read_raw_data(register) / self.ACCELERATION_SCALE_FACTOR

        def read_gyro(register):
            return read_raw_data(register) / self.GYRO_SCALE_FACTOR

        def roll(acc):
            return atan2(acc['ay'], acc['az']) * 180 / pi

        def pitch(acc):
            return atan2(acc['ax'], sqrt(pow(acc['ay'], 2) + pow(acc['az'], 2))) * 180 / pi

        acceleration = dict([(k, read_acceleration(v)) for (k, v) in self.ACCELERATION_REGISTERS.items()])
        gyro = dict([(k, read_gyro(v)) for (k, v) in self.GYRO_REGISTERS.items()])
        angles = {'roll': roll(acceleration), 'pitch': pitch(acceleration)}
        timestamp = {'t': time()}
        return {**acceleration, **gyro, **angles, **timestamp}


class ComplementaryFilter(object):
    def __init__(self, alpha=0.98):
        self.alpha = alpha
        self.beta = 1 - alpha
        self.t_minus_one = time()
        self.angles = dict()

    def update(self, measure):
        def filter_angle(angle_tag, acceleration_tag, gyro_tag):
            angle = self.angles.get(angle_tag, 0.0)
            acceleration = measure[acceleration_tag]
            gyro = measure[gyro_tag]
            return self.alpha * (angle + gyro * delta_t) + self.beta * acceleration

        delta_t = measure['t'] - self.t_minus_one
        self.t_minus_one = measure['t']
        result = measure
        result['pitch'] = self.angles['pitch'] = filter_angle('pitch', 'ax', 'gx')
        result['row'] = self.angles['row'] = filter_angle('row', 'ay', 'gy')
        return result
