from objects.resource import ResourceType
from objects.celestial import CelestialType
from objects.probemodule import Module


# How long a tick lasts
TICK_SLEEP_TIME = 1

# Probe Settings
TICK_LENGTH_TO_GENERATE = 10


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
    Module(name="solar panel", energy_cost=0, energy_generation=1, cost=2),
    Module(name="battery", energy_cost=0, energy_capacity=5, cost=2),
    Module(name="landing legs", energy_cost=1, allows_landing=True, cost=10),
    # TODO: Implement landing
    Module(name="scanner", energy_cost=1, allows_scanning=True, cost=5),
    # TODO: Implement scanning
    Module(name="drill", energy_cost=1, allows_mining=True, cost=10),
    # TODO: Implement Mining
    Module(name="radio scanner", energy_cost=3, allows_radio_scanning=True, cost=10),
    # TODO: Implement radio scanning
]

ENABLE_INTRO = True  # Toggles the pretty table at the top of the terminal
ENABLE_CHEATS = True
