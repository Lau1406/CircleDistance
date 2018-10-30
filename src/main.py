import random
import math

"""
Simple program to calculate the average distance of two random points on the circumference of a circle.
"""


class Point:
    """
    A simple point object. Has an x and a y coordinate
    """
    x = 1
    y = 1

    def __init__(self, x: float=1, y: float=1):
        self.x = x
        self.y = y


class Circle:
    """
    A simple circle object that has a radius
    """
    radius = 1

    def __init__(self, radius: float=1):
        self.radius = radius

    def get_point(self) -> Point:
        """
        Method to get a random point on the circumference of the circle
        :return: The point
        """

        # Get a random angle in radians
        angle = random.random() * 2 * math.pi

        return Point(math.cos(angle) * self.radius, math.sin(angle) * self.radius)


def distance(first: Point, second: Point) -> float:
    """
    Simple method to calculate the distance between two points
    :param first: The first point
    :param second: The second point
    :return: The distance as a float
    """
    dx = math.fabs(first.x - second.x)
    dy = math.fabs(first.y - second.y)
    return math.sqrt(dx**2 + dy**2)


def calculate_average_distance_points_circle(radius: float=1, amount: int=1000000) -> float:
    """
    Method to calculate the average distance of the points on a circle with radius r
    :param radius: The radius of the circle
    :param amount: The amount of tries to average over
    :return: The average distance as a float
    """
    total = 0
    circle = Circle(radius)

    for i in range(amount):
        first = circle.get_point()
        second = circle.get_point()
        total += distance(first, second)

    return total / amount


if __name__ == '__main__':
    print(calculate_average_distance_points_circle())
    print(4 / math.pi)
