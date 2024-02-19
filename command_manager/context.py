class Context:
    """
    Contains variables that commands may use
    """
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            self.add_kwarg(key, value)

    def add_kwarg(self, key, value):
        """
        Adds a new kwarg to this instance
        :param key: Key of the kwarg
        :param value: Value of the kwarg
        :return: None
        """
        setattr(self, key, value)
