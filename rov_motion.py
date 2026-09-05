import keyboard
import time


class thrusters:
    def __init__(self, thruster_id):
        self.speed = 0
        self.direction = None
        self.thruster_id = thruster_id

    def thrust_speed(self, thrust_id, speed):
        self.speed = speed
        self.thruster_id = thrust_id


class rov_motion:

    thruster1 = thrusters(1)
    thruster2 = thrusters(2)
    thruster3 = thrusters(3)
    thruster4 = thrusters(4)
    thruster5 = thrusters(5)
    thruster6 = thrusters(6)
    thruster7 = thrusters(7)
    thruster8 = thrusters(8)

    def rov_move_up(self, speed):
        self.thruster1.thrust_speed(1, speed)
        self.thruster2.thrust_speed(2, speed)
        self.thruster3.thrust_speed(3, speed)
        self.thruster4.thrust_speed(4, speed)
        self.thruster5.thrust_speed(5, speed)
        self.thruster6.thrust_speed(6, speed)
        self.thruster7.thrust_speed(7, speed)
        self.thruster8.thrust_speed(8, speed)

    def rov_move_down(self, speed):
        self.thruster1.thrust_speed(1, -speed)
        self.thruster2.thrust_speed(2, -speed)
        self.thruster3.thrust_speed(3, -speed)
        self.thruster4.thrust_speed(4, -speed)
        self.thruster5.thrust_speed(5, -speed)
        self.thruster6.thrust_speed(6, -speed)
        self.thruster7.thrust_speed(7, -speed)
        self.thruster8.thrust_speed(8, -speed)

    def rov_move_left(self, speed):
        self.thruster1.thrust_speed(1, -speed)
        self.thruster8.thrust_speed(8, -speed)
        self.thruster7.thrust_speed(7, speed)
        self.thruster2.thrust_speed(2, speed)
        self.thruster4.thrust_speed(4, -speed)
        self.thruster6.thrust_speed(6, -speed)
        self.thruster3.thrust_speed(3, speed)
        self.thruster5.thrust_speed(5, speed)

    def rov_move_right(self, speed):
        self.thruster1.thrust_speed(1, speed)
        self.thruster8.thrust_speed(8, speed)
        self.thruster7.thrust_speed(7, -speed)
        self.thruster2.thrust_speed(2, -speed)
        self.thruster4.thrust_speed(4, speed)
        self.thruster6.thrust_speed(6, speed)
        self.thruster3.thrust_speed(3, -speed)
        self.thruster5.thrust_speed(5, -speed)

    def rov_control_keyboard(self):
        print("Press the up arrow to move the ROV up")
        print("Press the down arrow to move the ROV down")
        print("Press the left arrow to move the ROV left")
        print("Press the right arrow to move the ROV right")

        while True:

            if keyboard.is_pressed("up"):
                self.rov_move_up(50)
                print("Moving up")
                time.sleep(0.2)
            elif keyboard.is_pressed("down"):
                self.rov_move_down(50)
                print("Moving down")
                time.sleep(0.2)
            elif keyboard.is_pressed("left"):
                self.rov_move_left(50)
                print("Moving left")
                time.sleep(0.2)
            elif keyboard.is_pressed("right"):
                self.rov_move_right(50)
                print("Moving right")
                time.sleep(0.2)
            else:
                self.thruster1.thrust_speed(1, 0)
                self.thruster2.thrust_speed(2, 0)
                self.thruster3.thrust_speed(3, 0)
                self.thruster4.thrust_speed(4, 0)
                self.thruster5.thrust_speed(5, 0)
                self.thruster6.thrust_speed(6, 0)
                self.thruster7.thrust_speed(7, 0)
                self.thruster8.thrust_speed(8, 0)
