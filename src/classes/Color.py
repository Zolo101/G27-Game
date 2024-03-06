class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __str__(self):
        return 'rgb(' + str(self.r) + ',' + str(self.g) + ',' + str(self.b) + ')'

    def __sub__(self, other):
        return Color(self.r - other.r, self.g - other.g, self.b - other.b)

    def __add__(self, other):
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)

    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b


