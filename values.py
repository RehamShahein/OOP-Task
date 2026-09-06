import random
import math


class random_values:
    def __init__(self, min_angle, max_angle, min_distance, max_distance):
        self.max_angle = max_angle
        self.min_angle = min_angle
        self.max_distance = max_distance
        self.min_distance = min_distance

    def generate_random_values(self):
        angle = random.uniform(self.min_angle, self.max_angle)
        distance = random.uniform(self.min_distance, self.max_distance)
        return angle, distance


class values_conversion:
    def __init__(self, angle, distance):
        self.angle = angle
        self.distance = distance

    def convert_to_cartesian(self):
        x = self.distance * math.cos(math.radians(self.angle))
        y = self.distance * math.sin(math.radians(self.angle))
        return x, y
