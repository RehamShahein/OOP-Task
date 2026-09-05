from health_monitor import health_monitor
from rov_motion import rov_motion

import time


class rov_system:
    def __init__(self):
        self.monitor = health_monitor()  # pylint: disable=invalid-name
        self.control = rov_motion()

    def start_system(self):
        while True:

            if self.monitor.health_check():
                print("System is healthy. Proceeding with ROV control.")
                time.sleep(2)
                print("Health check complete. Starting ROV control.")
                self.control.rov_control_keyboard()

            else:
                print("System is not healthy. Cooling down for 5 seconds.")
                time.sleep(5)
                print("cooling down complete. Rechecking system health.")
            time.sleep(2)


rov_system_instance = rov_system()
rov_system_instance.start_system()
