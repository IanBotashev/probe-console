import constants


class GameObject:
    """
    Adds an "update" function to a class that gets run every tick.
    """

    def __init__(self):
        # Position related
        self.x = 0
        self.y = 0

        # Run update() on each tick event
        constants.tick_manager.tick_event.subscribe(self.update)

    def update_position(self, new_x, new_y):
        """
        Updates this objects position
        :param new_x:
        :param new_y:
        :return: None
        """
        self.x = new_x
        self.y = new_y

    def update(self, tick):
        """
        This function gets run every tick.
        Meant to be overriden by child classes
        :param tick: The tick when this was run on
        :return: None
        """
        raise NotImplementedError("update function not implemented.")
