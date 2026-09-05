class health_monitor:
    def __init__(self, voltage, temperature, cpu_usage):
        self.voltage = voltage
        self.temperature = temperature
        self.cpu_usage = cpu_usage

    def health_check(self):
        if self.voltage < 4.5 or self.voltage > 5.5:
            return False
        if self.temperature < 0 or self.temperature > 70:
            return False
        if self.cpu_usage < 0 or self.cpu_usage > 1:
            return False
        else:
            return True
