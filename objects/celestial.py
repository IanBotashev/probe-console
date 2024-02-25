from dataclasses import dataclass
from objects.resource import ResourceSlot
import random
from engine.gameobject import GameObject


@dataclass
class CelestialType:
    """
    Types of celestial objects, how many slots they're allowed to have and what's the range of units for each
    slot.
    """
    # TODO: Add characteristics like surface temp, atmosphere, etc.
    name: str
    max_slots: int
    min_resource_units: int
    max_resource_units: int


class Celestial(GameObject):
    """
    Represents a celestial object, storing its type, slots and name.
    The type and name are required, but the slots can be generated AFTER object initialization.
    Or, they can also be set manually by doing something like self.slots = [slot1, slot2, slot3, ...]
    """
    def __init__(self,
                 name,
                 celestial_type: CelestialType,
                 revealed=False,
                 revealed_slots=False,):
        super().__init__()

        self.name = name
        self.type = celestial_type
        self.slots = None

        self.revealed = revealed  # Has this object been revealed?
        self.revealed_slots = revealed_slots  # Have its resources been scanned?

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
        if self.revealed_slots:
            return f"{self.type.name}(name={self.name}, resources={self.slots}, pos=({self.x}, {self.y}))"
        else:
            return f"{self.type.name}(name={self.name}, resources=unknown)"

    @staticmethod
    def generate(name, celestial_types, resources):
        """
        Randomly generates a celestial object. Requires all the possible types of resources and celestials
        :param name: Name for celestial
        :param celestial_types: All possible types to choose from
        :param resources: All resources to pick from
        :return:
        """
        result = Celestial(name=name,
                           celestial_type=random.choice(celestial_types))
        result.generate_slots(resources)
        return result
