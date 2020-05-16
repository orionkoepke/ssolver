import copy
import typing


class SudokuBoard:
    """
    SudokuBoard is a class that is capable of holding all the cells and their
    values on a Sudoku board.

    Cell - a square on a Sudoku board which can hold an integer value and whose position is
        denoted by the tuple (row, column)

    :ivar self._cells: a dictionary mapping row column pairs to the value in the cell
        (row, column) for all cells on the board whose values are known
    :ivar self._min_row_value: the minimum row number present on the Sudoku board
    :ivar self._max_row_value: the maximum row number present on the Sudoku board
    :ivar self._min_col_value: the minimum column number present on the Sudoku board
    :ivar self._max_col_value: the maximum column number present on the Sudoku board
    :ivar self._min_val_value: the minimum integer value a cell is capable of holding
        on the Sudoku board
    :ivar self._max_val_value: the maximum integer value a cell is capable of holding
        on the Sudoku board
    """

    def __init__(self):
        self._cells: typing.Dict[typing.Tuple[int, int], int] = {}

        self._min_row_value: int = 1
        self._max_row_value: int = 9

        self._min_col_value: int = 1
        self._max_col_value: int = 9

        self._min_val_value: int = 1
        self._max_val_value: int = 9

    def set_cell(self, row: int, column: int, value: int) -> None:
        if not (type(row) is int and self._min_row_value <= row <= self._max_row_value):
            raise ValueError(
                "The 'row' value %s is not an int in the range [%s, %s]"
                % (str(row), str(self._min_row_value), str(self._max_row_value))
            )

        elif not (type(column) is int and self._min_col_value <= column <= self._max_col_value):
            raise ValueError(
                "The 'column' value %s is not an int in the range [%s, %s]"
                % (str(column), str(self._min_col_value), str(self._max_col_value))
            )

        elif not (type(value) is int and self._min_val_value <= value <= self._max_val_value):
            raise ValueError(
                "The 'value' value %s is not an int in the range [%s, %s]"
                % (str(value), str(self._min_val_value), str(self._max_val_value))
            )

        else:
            self._cells[row, column] = value

    def remove_cell(self, row: int, column: int) -> typing.Union[int, None]:
        """
        remove_cell clears the value of the cell at (row, column) and returns its value if
        the cell had a value in the Sudoku board, otherwise it returns None

        :param row: the row coordinate of the cell whose value is to be removed
        :param column: the column coordinate of the cell whose value is to be removed

        :return: the value that was previously contained in the cell if the cell had a value
            on the Sudoku board, otherwise None
        """

        cell = None

        if (row, column) in self._cells:
            cell = self._cells[row, column]
            del self._cells[row, column]

        return cell

    def remove_all_cells(self) -> None:
        """
        remove_all_cells removes the value from every cell on the Sudoku board.

        :return: None
        """

        self._cells = {}

    def get_cell(self, row: int, column: int) -> typing.Union[int, None]:
        """
        get_cell returns the value contained in the cell at (row, column), or None if
        the cell does not currently contain a value on the Sudoku board.

        :param row: the row coordinate of the cell whose value is to be returned
        :param column: the column coordinate of the cell whose value is to be returned

        :return: the value contained in the cell at (row, column), or None if the cell
            does not currently contain a value on the Sudoku board
        """

        cell = None

        if (row, column) in self._cells:
            cell = self._cells[row, column]

        return cell

    def get_cells(self) -> typing.Dict[typing.Tuple[int, int], int]:
        """
        get_cells returns a deep copy of self._cells.

        :return: a deep copy of self._cells
        """

        return copy.deepcopy(self._cells)

    def __str__(self):
        board_str = ""

        for row in range(self._min_row_value, self._max_row_value + 1):
            for column in range(self._min_val_value, self._max_col_value + 1):
                board_str += "(%d, %d): %s\n" % (row, column, str(self.get_cell(row, column)))

        return board_str
