import random
from math import cos, sin, pi
import constants
from engine.gameobject.behavior import Behavior
from engine.gameobject import TickObject


class OrbitBehavior(TickObject, Behavior):
    """
    Allows a game object to start orbiting another gameobject at a certain radius and speed
    """

    def __init__(self, parent, orbit_object, radius, ticks_per_rotation, direction=1, angle_offset=0):
        """
        :param parent: The game object that this behavior is attached to
        :param orbit_object: The game object we should be orbiting around.
        :param radius: Radius of the orbit, measured in AU
        :param ticks_per_rotation: How many ticks there are per one full rotation
        :param direction: direction of orbit, 1 = counter-clockwise, -1 = clockwise.
        :param angle_offset: So we don't all start a 0, allows us to offset the orbit by a certain angle (radians)
        """
        Behavior.__init__(self, parent)
        TickObject.__init__(self)

        self.orbit_object = orbit_object
        self.radius = radius
        self.ticks_per_rotation = ticks_per_rotation
        self.angle_offset = angle_offset
        self.orbit_angle = angle_offset  # Essentially, at what angle from the parent object we are at. In radians.
        self.direction = direction

    def get_orbit_angle(self, tick):
        """
        Get the angle of the orbit at a certain time
        :param tick: Current tick
        :return: New angle
        """
        return (2 * pi * tick) / self.ticks_per_rotation + self.angle_offset

    def update(self, **kwargs):
        tick = constants.tick_manager.tick
        self.orbit_angle = self.get_orbit_angle(tick)
        self.game_object.update_position(
            cos(self.orbit_angle) * self.radius + self.orbit_object.x,
            sin(self.orbit_angle) * self.radius + self.orbit_object.y,
        )

    def __str__(self):
        return f"Orbit(radius={self.radius}, period={self.ticks_per_rotation}, direction={["counter-clockwise" if self.direction == 1 else "clockwise"][0]})"

    @staticmethod
    def generate_orbit(parent, orbit_object, radius):
        """
        Generates a new orbit object
        :param parent: Parent object this will be attached to
        :param orbit_object: Object to orbit around
        :param radius: Radius of the orbit to generate
        :return: OrbitingObject instance
        """
        ticks_per_rotation = random.uniform(300 * radius, 480 * radius)
        return OrbitBehavior(parent=parent,
                             orbit_object=orbit_object,
                             radius=radius,
                             ticks_per_rotation=ticks_per_rotation,
                             direction=random.choice([1, -1]),
                             angle_offset=random.uniform(0, ticks_per_rotation))
