from typing import List
from objects.celestial import Celestial
from engine.exceptions import InGameException
from engine.gameobject import GameObject
from settings import TICK_LENGTH_TO_GENERATE
from objects.probemodule import Module


class Probe(GameObject):
    def __init__(self, name: str, modules: List[Module]):
        super().__init__()
        self.name = name
        self.modules = modules

        # Energy
        self.energy = 0
        self.energy_cap = self.get_energy_capacity()
        self.energy_gen = self.get_energy_generation()

        # Location related
        self.location = None  # Which celestial object this is orbiting
        self.fuel = 5

        # Technical
        self.last_energy_update = 0

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
        :return: boolean if successful
        """
        if consume_fuel and self.fuel <= 0:
            raise InGameException("Probe does not have enough fuel to move locations.")

        if self.location == location:
            raise InGameException("Probe already at location.")

        self.location = location
        if consume_fuel:
            self.fuel -= 1

        return True

    def get_energy_capacity(self):
        """
        Goes through our modules and adds up the energy cap of each one
        :return:
        """
        result = 0
        for module in self.modules:
            result += module.energy_capacity
        return result

    def get_energy_generation(self):
        """
        Goes through our modules and adds up the energy generation of each one
        :return:
        """
        result = 0
        for module in self.modules:
            result += module.energy_generation
        return result

    def update(self, tick):
        # Update energy
        # Make sure it's been a certain amount of ticks since last update
        if self.last_energy_update + TICK_LENGTH_TO_GENERATE > tick:
            return
        # Make sure we don't go over the energy cap set by our modules
        if self.energy + self.energy_gen <= self.energy_cap:
            self.energy += self.energy_gen
        else:
            self.energy = self.energy_cap
        self.last_energy_update = tick

    @staticmethod
    def get_build_cost(modules):
        """
        Gets the build cost of the given modules
        :param modules:
        :return: Float of cost
        """
        result = 0
        for module in modules:
            result += module.cost

        return result

    def __str__(self):
        return f"{self.name}(energy=(stored={self.energy}, cap={self.energy_cap}, gen={self.energy_gen}), fuel={self.fuel}, location={self.location})"
