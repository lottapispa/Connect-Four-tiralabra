
class Minimizer():
    """Class that creates and keeps track of the minimizer."""
    def __init__(self):
        """Class constructor, creates variables."""
        self.pieces = 21
        self.color = "red"
        self.locations = [] # maybe as tuples (width, depth)
