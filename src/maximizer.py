
class Maximizer():
    """Class that creates and keeps track of the maximizer."""

    def __init__(self):
        """Class constructor, creates variables."""
        self.pieces = 21
        self.color = "blue"
        self.locations = []  # maybe as tuples (width, depth)
