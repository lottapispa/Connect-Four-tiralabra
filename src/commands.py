import keyboard

COMMANDS = {"0": "start the game"}


class Commands():
    """Class that handles key commands."""

    def __init__(self):
        pass

    def key_presses(self):
        while True:
            key = keyboard.read_key()
            if key not in COMMANDS:
                # print some type of error message
                continue
            if key == "0":
                pass
