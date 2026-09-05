import random


class mocksensor():
    def __init__(self, min_val=20.0, max_val=30.0):
        self.min_val = min_val
        self.max_val = max_val

    def read_value(self) -> float:
        #
        return round(random.uniform(self.min_val, self.max_val), 2)


class health_monitor:
    def __init__(self):
        self.voltage_sensor = mocksensor(4.0, 6.0)
        self.temperature_sensor = mocksensor(0.0, 70.0)
        self.cpu_usage_sensor = mocksensor(0.0, 1.0)

    def read_sensors(self):
        self.voltage = self.voltage_sensor.read_value()
        self.temperature = self.temperature_sensor.read_value()
        self.cpu_usage = self.cpu_usage_sensor.read_value()

    def health_check(self):
        self.read_sensors()

        if self.voltage < 4.5 or self.voltage > 5.5:
            print(f"Voltage out of range: {self.voltage}V")
            return False

        if self.temperature < 0 or self.temperature > 70:
            print(f"Temperature out of range: {self.temperature}°C")
            return False

        if self.cpu_usage < 0 or self.cpu_usage > 1:
            print(f"CPU usage out of range: {self.cpu_usage*100}%")
            return False

        else:
            print("All sensors are within acceptable ranges.")
            return True
