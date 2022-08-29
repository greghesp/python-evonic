from dataclasses import dataclass


@dataclass
class Network:
    ip: str
    subnet: str
    ssidAP: str
    signal_strength: str

    @staticmethod
    def from_dict(data):
        return Network(
            ip=data.get('ip'),
            subnet=data.get('subnet'),
            ssidAP=data.get('ssidAP'),
            signal_strength=data.get('dbm')
        )

    def update_from_dict(self, data):
        self.ip = data.get('ip', self.ip)
        self.subnet = data.get('subnet', self.subnet)
        self.ssidAP = data.get('ssidAP', self.ssidAP)
        self.signal_strength = data.get('dbm', self.signal_strength)


@dataclass
class Info:
    ssidAP: str
    configs: str
    product: str
    buildData: str
    fahrenheit: str
    last_ping: str

    @staticmethod
    def from_dict(data):
        return Info(
            ssidAP=data.get('ssidAP'),
            configs=data.get('configs'),
            product=data.get('product'),
            buildData=data.get('buildData'),
            fahrenheit=data.get('fahrenheit'),
            last_ping=data.get('time'),
        )

    def update_from_dict(self, data):
        self.ssidAP = data.get('ssidAP', self.ssidAP)
        self.configs = data.get('configs', self.configs)
        self.product = data.get('product', self.product)
        self.buildData = data.get('buildData', self.buildData)
        self.fahrenheit = data.get('fahrenheit', self.fahrenheit)
        self.last_ping = data.get('time', self.last_ping)


@dataclass
class Climate:
    current_temp: int
    target_temp: int
    heating: bool

    @staticmethod
    def from_dict(data):
        return Climate(
            current_temp=data.get('temperature'),
            target_temp=data.get('templevel'),
            heating=data.get('Heater')
        )

    def update_from_dict(self, data):
        self.current_temp = data.get('temperature', self.current_temp)
        self.target_temp = data.get('templevel', self.target_temp)
        self.heating = data.get('Heater', self.heating)


@dataclass
class Light:
    on: bool
    effect: str
    feature_light: bool
    flame_brightness: int
    flame_speed: int
    coal_brightness: int
    coal_speed: int

    @staticmethod
    def from_dict(data):
        return Light(
            on=data.get('Fire'),
            effect=data.get('effect'),
            feature_light=data.get('pinout3'),
            flame_brightness=data.get('brightnessRGB0'),
            flame_speed=data.get('speedRGB0'),
            coal_brightness=data.get('brightnessRGB1'),
            coal_speed=data.get('speedRGB1'),
        )

    def update_from_dict(self, data):
        self.on = data.get('Fire', self.on)
        self.effect = data.get('effect', self.effect)
        self.feature_light = data.get('pinout3', self.feature_light)
        self.flame_brightness = data.get('brightnessRGB0', self.flame_brightness)
        self.flame_speed = data.get('speedRGB0', self.flame_speed)
        self.coal_brightness = data.get('brightnessRGB1', self.coal_brightness)
        self.coal_speed = data.get('speedRGB1', self.coal_speed)


class Device:
    def __init__(self, data):
        self.info = Info.from_dict(data)
        self.climate = Climate.from_dict(data)
        self.network = Network.from_dict(data)
        self.light = Light.from_dict(data)

    def update_from_dict(self, data):
        self.info.update_from_dict(data)
        self.climate.update_from_dict(data)
        self.network.update_from_dict(data)
        self.light.update_from_dict(data)
        return self
