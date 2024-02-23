from dataclasses import dataclass
from typing import List
from objects.celestial import Celestial


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
        self.location = None  # Which celestial object this is orbiting
        self.fuel = 5

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

    def change_location(self, location: Celestial, consume_fuel: bool = True):
        """
        Changes the location of this probe to the given location
        Also checks if we have fuel and are not already at the specified location,
        if so, does nothing and prints to the console an error.
        :param location: Location to change the probe to
        :param consume_fuel: Decides whether or not to consume a unit of fuel to change location
        :return: None
        """
        if consume_fuel and self.fuel <= 0:
            print("Warning! This probe does not have enough fuel left to move location!")
            return

        if self.location == location:
            print("Already at location.")
            return

        self.location = location
        if consume_fuel:
            self.fuel -= 1


    def __str__(self):
        return f"{self.name}(energy={self.energy}, fuel={self.fuel}, location={self.location})"