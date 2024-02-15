#!/usr/bin/env python3.12
from gamemanager import GameManager
import os


def main():
    """
    Entrypoint for the game
    :return:
    """
    game_manager = GameManager()
    game_manager.main_loop()


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
