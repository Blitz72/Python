#!/usr/bin/python3

"""
This Python program is inspired from implementing the logic behind matrix
multiplication as found on the Wikipedia site:
https://en.wikipedia.org/wiki/Matrix_multiplication#
"""
from math import floor, log10
from typing import Self

class Matrix:
    def __init__(
        self,
        _cols: int,
        _rows: int,
        _data=None
    ) -> None:
        """
        ------------------------------------------------------------------------
        Initializes the Matrix object.

        Arguments:
            self (Matrix): The reference to this instance of the Matrix class.
            _cols (int): The number of columns in the matrix.
            _rows (int): The number of rows in the matrix.

        Keyword arguments:
            _data: The internal data of the _cols x _rows matrix in the form of
                a list of lists (default: None). For example:
                    self.data = [
                        [1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]
                    ]
        
        Returns:
            None
        ------------------------------------------------------------------------
        """
        self.cols = _cols
        self.rows = _rows
        if _data is None:
            self.data = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        else:
            if len(_data[0]) != self.cols or len(_data) != self.rows:
                raise IndexError(f'Matrix data must be a list of lists equal to the cols by rows ({self.cols} x {self.rows})!')
            self.data = _data

    def _largest_in_col(
        self,
        _col: int,
        _places: int
    ):
        """
        ------------------------------------------------------------------------
        Determines the largest value in the column and whether a negative value
        exists in the column to assist in printing.

        Arguments:
            self (Matrix): The reference to this instance of the Matrix class.
            _col (int): The column to check in the matrix.
            _places (int): The number of places to round float values to.

        Returns:
            largest: The largest value in the specific column of the matrix.
            neg (bool): Whether or not a negative number exists in the column.
        ------------------------------------------------------------------------
        """
        neg = False
        largest = 0
        for row in self.data:
            if abs(row[_col]) > largest:
                largest = abs(row[_col])
            if round(row[_col], _places) < 0:
                neg = True
        return largest, neg

    def add(
        self,
        _matrix: Self
    ) -> Self:
        """
        ------------------------------------------------------------------------
        Adds the values of the natrix that is passed in to this matrix.

        Arguments:
            self (Matrix): The reference to this instance of the Matrix class.
            _matrix (Matrix): The matrix to add to this matrix.

        Returns:
            A new matrix with the values of _matrix added to this matrix.
        ------------------------------------------------------------------------
        """
        assert(self.cols == _matrix.cols and self.rows == _matrix.rows)
        new_matrix = Matrix(self.cols, self.rows)
        for y in range(self.rows):
            for x in range(self.cols):
                new_matrix.data[x][y] = self.data[x][y] + _matrix.data[x][y]
        return new_matrix

    def multiply(
        self,
        _matrix: Self
    ) -> Self:
        """
        ------------------------------------------------------------------------
        Multiplies this matrix by the _matrix that is passed in.

        Arguments:
            self (Matrix): The reference to this instance of the Matrix class.
            _matrix (Matrix): The matrix to multiply this matrix by.

        Returns:
            A new matrix containing the result of the matrix multiplication.
        ------------------------------------------------------------------------
        """
        assert(self.cols == _matrix.rows)
        new_matrix = Matrix(_matrix.cols, self.rows)
        for y in range(self.rows):
            for x in range(len(_matrix.data[0])):
                for z in range(len(self.data[0])):
                    new_matrix.data[y][x] += self.data[y][z] * _matrix.data[z][x]
        return new_matrix

    def print(
        self,
        _places: int = 0
    ) -> None:
        """
        ------------------------------------------------------------------------
        Prints the matrix in a readable format such as:
            | 1 2 3 |
            | 4 5 6 |
            | 7 8 9 |

        Arguments:
            self (Matrix): The reference to this instance of the Matrix class.

        Keyword arguments:
            _places (int): The number of places to use when printing floats
                (default: 0).
        
        Returns:
            None.
        ------------------------------------------------------------------------
        """
        largest_dict = {}
        print()
        for col in range(len(self.data[0])):
            largest_dict[col] = {}
            largest_dict[col]['largest'], largest_dict[col]['neg'] = self._largest_in_col(col, _places)
        # print(largest_dict)
        for row in self.data:
            # TODO: Refactor so the mathematical processes involved don't take
            # down the power grid for the Eastern seaboard for a matrix larger
            # than 4x4!!!
            print('|', end=' ')
            for col in range(len(row)):
                largest = largest_dict[col]['largest']
                neg = largest_dict[col]['neg']
                largest = round(largest, _places) if round(largest, _places) != 0.0 else 1  # log10(num), where num is not zero
                value_to_print = round(row[col], _places) if round(row[col], _places) != 0.0 else abs(round(row[col], _places)) # Do not print -0.0, print 0.0
                value_for_end = round(row[col], _places) if round(row[col], _places) != 0.0 else 1    # log10(num), where num is not zero
                if isinstance(value_for_end, int):
                    end_spaces = ' ' * (floor(log10(largest)) - floor(log10(abs(value_for_end))) + 1)
                else:
                    end_spaces = ' ' * (floor(log10(largest)) - floor(log10(abs(value_for_end))) + 1) if floor(log10(abs(value_for_end))) >= 0 else ' '
                fmt_str = '{: .' +str(_places) + 'f}' if neg else '{:.' +str(_places) + 'f}'
                print(fmt_str.format(value_to_print), end=end_spaces)
            print('|')

    def subtract(
        self,
        _matrix: Self
    ) -> Self:
        """
        ------------------------------------------------------------------------
        Subtracts the values of the natrix that is passed in from this matrix.

        Arguments:
            self (Matrix): The reference to this instance of the Matrix class.
            _matrix (Matrix): The matrix to subtract from this matrix.

        Returns:
            A new matrix with the values of _matrix subtracted from this matrix.
        ------------------------------------------------------------------------
        """
        assert(self.cols == _matrix.cols and self.rows == _matrix.rows)
        new_matrix = Matrix(self.cols, self.rows)
        for y in range(self.rows):
            for x in range(self.cols):
                new_matrix.data[x][y] = self.data[x][y] - _matrix.data[x][y]
        return new_matrix

    def transpose(
        self
    ) -> None:
        """
        ------------------------------------------------------------------------
        Transposes this matrix. For example:
            | 1 2 3 |  -->  | 1 4 |
            | 4 5 6 |       | 2 5 |
                            | 3 6 |

        Arguments:
            self (Matrix): The reference to this instance of the Matrix class.

        Returns:
            None.
        ------------------------------------------------------------------------
        """
        matrix_transposed = Matrix(self.rows, self.cols)
        for j in range(self.rows):
            for i in range(self.cols):
                matrix_transposed.data[i][j] = self.data[j][i]
        self.cols = matrix_transposed.cols
        self.rows = matrix_transposed.rows
        self.data = matrix_transposed.data

if __name__ == "__main__":
    matrix_a = Matrix(
        3,
        4
    )
    matrix_a.data = [
        [1, 0, 1],
        [2, 1, 1],
        [0, 1, 1],
        [1, 1, 2],
    ]
    print(matrix_a.data)
    matrix_a.print()

    data = [
        [1, 2, 1],
        [2, 3, 1],
        [4, 2, 2]
    ]
    matrix_b = Matrix(
        3,
        3,
        data
    )
    print(matrix_b.data)
    matrix_b.print()

    matrix_c = matrix_a.multiply(matrix_b)
    matrix_c.print()
    
    matrix_d = Matrix(
        1,
        3,
        [
            [100],
            [80],
            [60]
        ]
    )
    matrix_d.print()
    
    matrix_e = matrix_c.multiply(matrix_d)
    matrix_e.print()

    matrix_f = Matrix(
        2,
        2,
        [
            [4, 7],
            [2, 6]
        ]
    )
    matrix_f.print()
    # matrix_f.multiply(matrix_a)

    matrix_g = Matrix(
        2,
        2,
        [
            [0.6, -0.7],
            [-0.2, 0.4]
        ]
    )
    matrix_g.print()

    matrix_h = Matrix(
        2,
        2,
        [
            [1.23, 4.56],
            [7.89, 10.11]
        ]
    )
    matrix_h.print()
    matrix_h.print(_places=2)

    matrix_i = matrix_f.multiply(matrix_g)
    matrix_i.print()
    matrix_i.print(_places=20)

    matrix_j = matrix_g.multiply(matrix_h)
    matrix_j.print()
    matrix_j.print(_places=4)

    matrix_j.transpose()
    matrix_j.print(_places=4)

    matrix_a.print()
    matrix_a.transpose()
    matrix_a.print()

    matrix_k = Matrix(
        3,
        3,
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    )

    matrix_b.print()
    matrix_k.print()
    matrix_l = matrix_b.add(matrix_k).print()
    matrix_m = matrix_b.subtract(matrix_k).print()
    # matrix_l.print()
