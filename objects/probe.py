from dataclasses import dataclass
from typing import List


@dataclass
class Module:
    """
    Represents a module that can be equipped on a probe
    """
    name: str
    energy_cost: int
    energy_capacity: int  # Only for modules that store energy, A.K.A. batteries
    energy_generation: int  # Only for modules that generate energy, A.K.A. solar panels

    # Variables that turn on/off abilities of the probe
    allows_mining: bool
    allows_landing: bool
    allows_scanning: bool


class Probe:
    def __init__(self, name: str, modules: List[Module]):
        self.name = name
        self.modules = modules
        self.energy = 0

    def can_mine(self):
        """
        Checks all the modules and checks if any of them allow mining
        :return: A boolean indicating whether or not the probe can mine
        """
        for module in self.modules:
            if module.allows_mining:
                return True

        return False

    def can_land(self):
        """
        Checks all the modules and checks if any of them allow landing
        :return: A boolean indicating whether or not this probe can land
        """
        for module in self.modules:
            if module.allows_landing:
                return True

        return False

    def can_scan(self):
        """
        Checks all the modules and checks if any of them allow scanning
        :return: A boolean indicating whether or not this probe can scan
        """
        for module in self.modules:
            if module.allows_scanning:
                return True

        return False
