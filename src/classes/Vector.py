import math


class Vector:
    """ A 2D Vector. """

    def __init__(self, x=0, y=0):
        """ Initializer """
        self.x = x
        self.y = y

    def __str__(self):
        """ Returns a string representation of the vector """
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __eq__(self, other):
        """ Tests the equality of this vector and another """
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """ Tests the inequality of this vector and another """
        return not self.__eq__(other)

    def get_p(self):
        """ Returns a tuple with the point corresponding to the vector """
        return (self.x, self.y)

    def copy(self):
        """ Returns a copy of the vector """
        return Vector(self.x, self.y)

    def add(self, other):
        """ Adds another vector to this vector """
        self.x += other.x
        self.y += other.y
        return self

    def __add__(self, other):
        return self.copy().add(other)

    def negate(self):
        """ Negates the vector (makes it point in the opposite direction) """
        return self.multiply(-1)

    def __neg__(self):
        return self.copy().negate()

    def subtract(self, other):
        """ Subtracts another vector from this vector """
        return self.add(-other)

    def __sub__(self, other):
        return self.copy().subtract(other)

    def multiply(self, k):
        """ Multiplies the vector by a scalar """
        self.x *= k
        self.y *= k
        return self

    def __mul__(self, k):
        return self.copy().multiply(k)

    def __rmul__(self, k):
        return self.copy().multiply(k)

    def divide(self, k):
        """ Divides the vector by a scalar """
        return self.multiply(1 / k)

    def __truediv__(self, k):
        return self.copy().divide(k)

    def normalize(self):
        """ Normalizes the vector """
        return self.divide(self.length())

    def get_normalized(self):
        """ Returns a normalized version of the vector """
        return self.copy().normalize()

    def dot(self, other):
        """ Returns the dot product of this vector with another one """
        return self.x * other.x + self.y * other.y

    def length(self):
        """ Returns the length of the vector """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def length_squared(self):
        """ Returns the squared length of the vector """
        return self.x ** 2 + self.y ** 2

    def reflect(self, normal):
        """ Reflect this vector on a normal """
        n = normal.copy()
        n.multiply(2 * self.dot(normal))
        self.subtract(n)
        return self

    def angle(self, other):
        """ Returns the angle between this vector and another one """
        return math.acos(self.dot(other) / (self.length() * other.length()))

    def rotate_anti(self):
        """ Rotates the vector 90 degrees anticlockwise """
        self.x, self.y = -self.y, self.x
        return self

    def rotate_rad(self, theta):
        """ Rotates the vector according to an angle theta given in radians """
        rx = self.x * math.cos(theta) - self.y * math.sin(theta)
        ry = self.x * math.sin(theta) + self.y * math.cos(theta)
        self.x, self.y = rx, ry
        return self

    def rotate(self, theta):
        """ Rotates the vector according to an angle theta given in degrees """
        theta_rad = theta / 180 * math.pi
        return self.rotate_rad(theta_rad)

    def get_proj(self, vec):
        """ Project the vector onto a given vector """
        unit = vec.get_normalized()
        return unit.multiply(self.dot(unit))

    def minimum(self, vec):
        """ Returns the minimum of the two vectors """
        return Vector(min(self.x, vec.x), min(self.y, vec.y))

    def maximum(self, vec):
        """ Returns the maximum of the two vectors """
        return Vector(max(self.x, vec.x), max(self.y, vec.y))

    def clamp(self, min_vec, max_vec):
        """ Clamps the vector to a given vector """
        return self.minimum(max_vec).maximum(min_vec)