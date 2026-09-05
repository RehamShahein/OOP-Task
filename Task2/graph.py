from values import random_values, values_conversion
import matplotlib.pyplot as plt


class values_for_graph:
    def __init__(self, min_angle, max_angle, min_distance, max_distance):
        self.randomizer = random_values(
            min_angle, max_angle, min_distance, max_distance)

    def get_random_cartesian_coordinates(self):
        angle, distance = self.randomizer.generate_random_values()
        position = values_conversion(angle, distance)
        x, y = position.convert_to_cartesian()
        print(f"Random Angle: {angle:.2f} degrees")
        print(f"Random Distance: {distance:.2f} units")
        print(f"Converted Cartesian Coordinates: x = {x:.2f}, y = {y:.2f}")
        return x, y


class graph:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def plot(self):

        plt.scatter(self.x, self.y)
        plt.title(f'Random Points in Cartesian Coordinates')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.grid()
        plt.axis('equal')
        plt.axvline(x=0, color='black', linewidth=0.5)
        plt.axhline(y=0, color='black', linewidth=0.5)
        plt.show()


values = values_for_graph(min_angle=0, max_angle=360,
                          min_distance=0, max_distance=10)
x, y = values.get_random_cartesian_coordinates()


graph_done = graph(x, y)
graph_done.plot()
