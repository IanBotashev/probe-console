from objects.resource import ResourceType
from objects.celestial import CelestialType
from objects.probe import Module


# How long a tick lasts
TICK_SLEEP_TIME = 1


# All resource types that can be found in-game and their sell value
RESOURCES = [
    ResourceType("gold", 50),
    ResourceType("iron", 5),
    ResourceType("lead", 10),
    ResourceType("copper", 10),
]

# All types of celestials possible in-game
CELESTIAL_TYPES = [
    CelestialType("asteroid", 1, 1, 20),
    CelestialType("moon", 2, 5, 25),
    CelestialType("planet", 3, 10, 30)
]


# All types of modules that can be found in-game
MODULES = [
    Module(name="solar panel", energy_cost=0, energy_capacity=0, energy_generation=1, allows_mining=False, allows_landing=False, allows_scanning=False),
    Module(name="battery", energy_cost=0, energy_capacity=5, energy_generation=0, allows_mining=False, allows_landing=False, allows_scanning=False),
    Module(name="landing legs", energy_cost=1, energy_capacity=0, energy_generation=0, allows_mining=False, allows_landing=True, allows_scanning=False),
    Module(name="scanner", energy_cost=1, energy_capacity=0, energy_generation=0, allows_mining=False, allows_landing=False, allows_scanning=True),
    Module(name="drill", energy_cost=1, energy_capacity=0, energy_generation=0, allows_mining=True, allows_landing=False, allows_scanning=False),
]
