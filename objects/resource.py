from dataclasses import dataclass
import random
from typing import List


@dataclass
class ResourceType:
    name: str
    sell_value: float


class ResourceSlot:
    """
    Keeps track of one singular resource slot, storing the resource and units left
    """
    def __init__(self, resource_type: ResourceType, units):
        self.type = resource_type
        self.units = units

    def __str__(self):
        return f"Resource Slot(type: {self.type}, units: {self.units}, value: {self.type.sell_value * self.units})"

    def __repr__(self):
        return self.type.name

    @staticmethod
    def generate(min_units: int, max_units: int, resources: List[ResourceType]):
        """
        Generates a random resource slot
        :param min_units: Minimum amount of units this slot will have
        :param max_units: Maximum amount of units this slot will have
        :param resources: Resource to pick from
        :return:
        """
        return ResourceSlot(random.choice(resources), random.randint(min_units, max_units))
