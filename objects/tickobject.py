class TickObject:
    """
    Adds an "update" function to a class that gets run every tick.
    """
    def update(self, tick):
        """
        This function gets run every tick.
        :param tick: The tick when this was run on
        :return: None
        """
        raise NotImplementedError("update function not implemented.")
