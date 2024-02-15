from objects.resource import ResourceType
from objects.celestial import CelestialType


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
    CelestialType("asteroid", 3, 10, 30)
]
