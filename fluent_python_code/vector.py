# Example of implementing numerical operations such as + and *
# For A Vector of (x,y) coordinates

from math import hypot


class Vector:
    """Two dimensional vector class"""

    def __init__(self, x: float = 0, y: float = 0):
        """Initialize the Vector

        Args:
            x (float, optional): The X coordinate of the vector. Defaults to 0.
            y (float, optional): The Y coordinate of the vector. Defaults to 0.
        """
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        """Return the representation of a Vector object

        Returns:
            str: The representation string of a Vector object.
        """
        return f"Vector({self.x}, {self.y})"

    def __abs__(self) -> float:
        """Returns the length of the vector starting from the (0,0) position

        Returns:
            float: the length of the vector.
        """
        return hypot(self.x, self.y)

    def __bool__(self) -> bool:
        """The truth value of a vector, it is defined so:
        length of vector = 0 => False
        length of vector > 0 => True

        Returns:
            bool: The truth value of a vector
        """
        return bool(abs(self))

    def __add__(self, other: Vector) -> Vector:
        """Adds one vector object to another

        Args:
            other (Vector): The other vector to be added to the current one.

        Returns:
            Vector: A newly created vector that has coordinates
            equal to the sum of the two added vectors
        """
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar: float) -> Vector:
        """Multiples vectors with a certain scalar

        Args:
            scalar (float): The scalar that multiplies the vector

        Returns:
            Vector: A newly created vector with coordinated equal to the initial
            vector but coordinates are multiplied by the scalar
        """
        return Vector(self.x * scalar, self.y * scalar)
