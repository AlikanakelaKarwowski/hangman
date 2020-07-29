from os import system, name


def hang(number):
    switcher = {
        0: hangman,
        1: hangman_head,
        2: hangman_body,
        3: hangman_arm1,
        4: hangman_arm2,
        5: hangman_leg1,
        6: hangman_leg2,
        7: game_over
    }
    switch = switcher.get(number)
    return switch()


def game_over():
    print("Game Over")


def hangman():
    print("          __________",
          "\n         |         |",
          "\n         |         |",
          "\n                   |",
          "\n                   |",
          "\n                   |",
          "\n                   |",
          "\n                   |",
          "\n                   |",
          "\n                   |",
          "\n                   |",
          "\n                   |",
          "\n      _____________|_____",
          "\n                           ")


def hangman_head():
    print("          __________",
          "\n         |         |",
          "\n         |         |",
          "\n       _/_\_       |",
          "\n        |_|        |",
          "\n                   |",
          "\n                   |",
          "\n                   |",
          "\n                   |",
          "\n                   |",
          "\n                   |",
          "\n                   |",
          "\n      _____________|_____",
          "\n                           ")


def hangman_body():
    print("          __________",
          "\n         |         |",
          "\n         |         |",
          "\n       _/_\_       |",
          "\n        |_|        |",
          "\n         |         |",
          "\n         |         |",
          "\n         |         |",
          "\n         |         |",
          "\n                   |",
          "\n                   |",
          "\n                   |",
          "\n      _____________|_____",
          "\n                           ")


def hangman_arm1():
    print("          __________",
          "\n         |         |",
          "\n         |         |",
          "\n       _/_\_       |",
          "\n        |_|        |",
          "\n         |         |",
          "\n      ---|         |",
          "\n         |         |",
          "\n         |         |",
          "\n                   |",
          "\n                   |",
          "\n                   |",
          "\n      _____________|_____",
          "\n                           ")


def hangman_arm2():
    print("          __________",
          "\n         |         |",
          "\n         |         |",
          "\n       _/_\_       |",
          "\n        |_|        |",
          "\n         |         |",
          "\n      ---|---      |",
          "\n         |         |",
          "\n         |         |",
          "\n                   |",
          "\n                   |",
          "\n                   |",
          "\n      _____________|_____",
          "\n                           ")


def hangman_leg1():
    print("          __________",
          "\n         |         |",
          "\n         |         |",
          "\n       _/_\_       |",
          "\n        |_|        |",
          "\n         |         |",
          "\n      ---|---      |",
          "\n         |         |",
          "\n         |         |",
          "\n        /          |",
          "\n       /           |",
          "\n                   |",
          "\n      _____________|_____",
          "\n                           ")


def hangman_leg2():
    print("          __________",
          "\n         |         |",
          "\n         |         |",
          "\n       _/_\_       |",
          "\n        |_|        |",
          "\n         |         |",
          "\n      ---|---      |",
          "\n         |         |",
          "\n         |         |",
          "\n        / \        |",
          "\n       /   \       |",
          "\n                   |",
          "\n      _____________|_____",
          "\n                           ")


# define our clear function
def clear_screen():
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
