import constants
from engine.gameobject.behavior import Behavior


class GameObject:
    """
    Adds an "update" function to a class that gets run every tick.
    Also
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.behaviors = []

    def add_behavior(self, behavior: Behavior):
        """
        Adds a behavior to this game object. Sets the behavior to active
        :param behavior: Behavior to add
        :return: None
        """
        self.behaviors.append(behavior)
        behavior.active = True

    def remove_behavior(self, behavior: Behavior):
        """
        Removes a behavior from this game object, sets it to be inactive.
        :param behavior: Behavior to remove
        :return: None
        """
        self.behaviors.remove(behavior)
        behavior.active = False

    def update_position(self, new_x, new_y):
        """
        Updates this objects position
        :param new_x:
        :param new_y:
        :return: None
        """
        self.x = new_x
        self.y = new_y


class TickObject:
    """
    Adds an update function that gets ran every tick.
    """
    def __init__(self):
        constants.tick_manager.tick_event.subscribe(self.update)

    def update(self, **kwargs):
        """
        This gets ran every tick
        :param kwargs:
        :return:
        """
        raise NotImplemented("update() not implemented")
