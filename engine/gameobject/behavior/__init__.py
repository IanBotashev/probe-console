class Behavior:
    """
    Allows game objects to inherit behaviors, like orbiting around another game object.
    """
    def __init__(self, game_object):
        """
        :param game_object:
        """
        self.game_object = game_object
