from dataclasses import dataclass
from objects.resource import ResourceSlot
import random


@dataclass
class CelestialType:
    """
    Types of celestial objects, how many slots they're allowed to have and what's the range of units for each
    slot.
    """
    name: str
    max_slots: int
    min_resource_units: int
    max_resource_units: int


class Celestial:
    """
    Represents a celestial object, storing it's type, slots and name.
    The type and name are required, but the slots can be generated AFTER object initialization.
    Or, they can also be set manually by doing something like self.slots = [slot1, slot2, slot3, ...]
    """
    def __init__(self, name, celestial_type: CelestialType):
        self.name = name
        self.type = celestial_type
        self.slots = None

    def generate_slots(self, resources):
        """
        Generate a set of slots for this object, taking into consideration how many slots this type can have.
        :param resources: What resources to pick from
        :return:
        """
        self.slots = []
        for _ in range(self.type.max_slots):
            slot = ResourceSlot.generate(self.type.min_resource_units, self.type.max_resource_units, resources)
            self.slots.append(slot)

    def __str__(self):
        return f"Celestial(name={self.name}, type={self.type})"

    @staticmethod
    def generate(celestial_types, resources):
        """
        Randomly generates a celestial object. Requires all the possible types of resources and celestials
        :return:
        """
        # TODO: add name generation or just ask for one
        result = Celestial(name="some cool name",
                           celestial_type=random.choice(celestial_types))
        result.generate_slots(resources)
        return result
