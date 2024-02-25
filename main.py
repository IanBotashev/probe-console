#!/usr/bin/env python3.12
from engine.game import Game
import os
import constants


# TODO: Add a rough "map", putting on it probes and celestials

def main():
    """
    Entrypoint for the game
    :return:
    """
    constants.game = Game()
    constants.game.run()


def clear_terminal():
    """
    Clears the terminal
    :return:
    """
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Unix/Linux/MacOS
    else:
        os.system('clear')


if __name__ == "__main__":
    clear_terminal()
    try:
        main()
    except KeyboardInterrupt:
        print('goodbye...')
