#!/usr/bin/python3

class Coordinate(object):
	"""
	A class for handling rectangular vector coordinates and basic vector math.
	"""
	def __init__(self, x, y):
		"""
		Initializes a rectangular coordinate.

		Args:
			x (int): The x value of the Coordinate.
			y (int): The y value of the Coordinate.
		Returns:
			None:
		"""
		self.x = x
		self.y = y

	def __str__(self):
		return f'<{self.x}, {self.y}>'

	def __repr__(self):
		return f'Coordinate(x={self.x}, y={self.y})'

	def __add__(a, b):
		return Coordinate.vector_add(a, b)

	def __sub__(a, b):
		return Coordinate.vector_sub(a, b)

	def distance_from(self, other):
		"""
		Calculates the distance from this Coordinate to another Coordinate.

		Args:
			other (Coordinate): The Coordinate from which distance is calculated.
		Returns:
			float: The distance between the two Coordinates.
		"""
		dist_x_sq = (self.x - other.x) ** 2
		dist_y_sq = (self.y - other.y) ** 2
		return (dist_x_sq + dist_y_sq) ** 0.5

	def vector_add(self, other):
		"""
		Adds two Coordinate vectors together.

		Args:
			other (Coordinate): The Coordinate to be added to this Coordinate.
		Returns:
			Coordinate: The value of the summed Coordinates.
		"""
		new_x = self.x + other.x
		new_y = self.y + other.y
		return Coordinate(new_x, new_y)

	def vector_sub(self, other):
		"""
		Subtracts two Coordinate vectors.

		Args:
			other (Coordinate): The Coordinate to be subtracted from this
			                    Coordinate.
		Returns:
			Coordinate: The value of subtracting the two 
			Coordinates.
		"""
		new_x = self.x - other.x
		new_y = self.y - other.y
		return Coordinate(new_x, new_y)


if __name__ == '__main__':
	vector_1 = Coordinate(1, 2)
	vector_2 = Coordinate(4, 6)
	print(vector_1)
	print(vector_2)
	print(vector_1.__repr__())
	print(vector_2.__repr__())
	print(vector_1.vector_sub(vector_2))
	print(vector_1.distance_from(vector_2))
