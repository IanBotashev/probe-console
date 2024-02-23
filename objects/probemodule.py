from dataclasses import dataclass


@dataclass
class Module:
    """
    Represents a module that can be equipped on a probe
    """
    name: str
    energy_cost: int
    energy_capacity: int  # Only for modules that store energy, A.K.A. batteries
    energy_generation: int  # Only for modules that generate energy, A.K.A. solar panels
    cost: int  # Dollar cost to use this module

    # Variables that turn on/off abilities of the probe
    allows_mining: bool
    allows_landing: bool
    allows_scanning: bool
    allows_radio_scanning: bool
