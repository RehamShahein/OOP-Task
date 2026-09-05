from health_monitor import health_monitor
from rov_motion import rov_motion

import time


class rov_system:
    def __init__(self, voltage=5.0, temperature=25.0, cpu_usage=0.5):
        self.monitor = health_monitor(voltage, temperature, cpu_usage)
        self.control = rov_motion()

    def start_system(self):
        if self.monitor.health_check():
            print("System is healthy. Proceeding with ROV control.")
            self.control.rov_control_keyboard()

        else:
            print("System is not healthy. Cooling down for 5 seconds.")
            time.sleep(5)


rov_system_instance = rov_system()
rov_system_instance.start_system()
