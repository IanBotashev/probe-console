# This file defines variables that should be accessible from any part of the project
# Such as the game manager, game, or even tick system.
# They can also be modified, which should be kept in mind when accessing them.
# We can't use settings.py, as it imports files that may need to access itself, creating circular import excs.

game = None  # Points to instance of the game class
game_manager = None  # Points to instance of the game manager
tick_manager = None  # Points to instance of the tick manager
player = None  # Points to instance of the Player class.
