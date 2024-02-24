from dataclasses import dataclass


@dataclass
class Module:
    """
    Represents a module that can be equipped on a probe
    """
    name: str
    energy_cost: int
    cost: int  # Dollar cost to use this module
    energy_capacity: int = 0  # Only for modules that store energy, A.K.A. batteries
    energy_generation: int = 0  # Only for modules that generate energy, A.K.A. solar panels

    # Variables that turn on/off abilities of the probe
    allows_mining: bool = False
    allows_landing: bool = False
    allows_scanning: bool = False
    allows_radio_scanning: bool = False
