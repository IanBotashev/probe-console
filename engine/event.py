class Event:
    """
    Allows functions to be called when an event is triggered.
    """
    def __init__(self):
        self.subscribers = []

    def subscribe(self, function):
        """
        Subscribe function to this event
        :param function: Function to be subscribed
        :return: None
        """
        self.subscribers.append(function)

    def unsubscribe(self, function):
        """
        Unsubscribe from this event
        :param function: Function to be unsubscribed
        :return: None
        """
        self.subscribers.remove(function)

    def trigger(self, *args, **kwargs):
        """
        Trigger this event and run its subscribers
        Pass args and kwargs to its subscribers when ran as well
        :return: None
        """
        for subscriber in self.subscribers:
            subscriber(*args, **kwargs)
