import copy
import unittest

from ssolver.sudoku_board import SudokuBoard


class TestSudokuBoardInit(unittest.TestCase):

    def test___init___1(self):
        sb = SudokuBoard()

        self.assertDictEqual(
            sb.__dict__,
            {
                "_cells": {},
                "_min_row_value": 1,
                "_max_row_value": 9,
                "_min_col_value": 1,
                "_max_col_value": 9,
                "_min_val_value": 1,
                "_max_val_value": 9
            }
        )


class TestSudokuBoardSetCell(unittest.TestCase):

    def test_set_cell_1(self):
        sb = SudokuBoard()

        start_state = copy.deepcopy(sb.__dict__)

        sb.set_cell(1, 2, 3)

        self.assertDictEqual(
            sb.__dict__,
            {
                **start_state,
                "_cells": {
                    (1, 2): 3,
                },
            }
        )

    def test_set_cell_2(self):
        sb = SudokuBoard()

        start_state = copy.deepcopy(sb.__dict__)

        sb.set_cell(1, 2, 3)
        sb.set_cell(2, 3, 4)

        self.assertDictEqual(
            sb.__dict__,
            {
                **start_state,
                "_cells": {
                    (1, 2): 3,
                    (2, 3): 4,
                },
            }
        )

    def test_set_cell_3(self):
        sb = SudokuBoard()

        start_state = copy.deepcopy(sb.__dict__)

        sb.set_cell(1, 2, 3)
        sb.set_cell(1, 2, 4)

        self.assertDictEqual(
            sb.__dict__,
            {
                **start_state,
                "_cells": {
                    (1, 2): 4,
                },
            }
        )

    def test_set_cell_4(self):
        sb = SudokuBoard()

        start_state = copy.deepcopy(sb.__dict__)

        try:
            sb.set_cell(sb._max_row_value + 1, 2, 3)

        except ValueError as exception:
            self.assertEqual(
                str(exception),
                "The 'row' value %s is not an int in the range [%s, %s]"
                % (str(sb._max_row_value + 1), str(sb._min_row_value), str(sb._max_row_value))
            )

        else:
            self.fail("A ValueError was expected.")

        self.assertDictEqual(
            sb.__dict__,
            start_state
        )

    def test_set_cell_5(self):
        sb = SudokuBoard()

        start_state = copy.deepcopy(sb.__dict__)

        sb.set_cell(1, 2, 6)

        try:
            sb.set_cell(sb._max_row_value + 1, 2, 3)

        except ValueError as exception:
            self.assertEqual(
                str(exception),
                "The 'row' value %s is not an int in the range [%s, %s]"
                % (str(sb._max_row_value + 1), str(sb._min_row_value), str(sb._max_row_value))
            )

        else:
            self.fail("A ValueError was expected.")

        self.assertDictEqual(
            sb.__dict__,
            {
                **start_state,
                "_cells": {
                    (1, 2): 6,
                },
            }
        )
        
    def test_set_cell_6(self):
        sb = SudokuBoard()

        start_state = copy.deepcopy(sb.__dict__)

        try:
            sb.set_cell(1, sb._max_col_value + 1, 3)

        except ValueError as exception:
            self.assertEqual(
                str(exception),
                "The 'column' value %s is not an int in the range [%s, %s]"
                % (str(sb._max_col_value + 1), str(sb._min_col_value), str(sb._max_col_value))
            )

        else:
            self.fail("A ValueError was expected.")

        self.assertDictEqual(
            sb.__dict__,
            start_state
        )

    def test_set_cell_7(self):
        sb = SudokuBoard()

        start_state = copy.deepcopy(sb.__dict__)

        sb.set_cell(1, 2, 6)

        try:
            sb.set_cell(1, sb._max_col_value + 1, 3)

        except ValueError as exception:
            self.assertEqual(
                str(exception),
                "The 'column' value %s is not an int in the range [%s, %s]"
                % (str(sb._max_col_value + 1), str(sb._min_col_value), str(sb._max_col_value))
            )

        else:
            self.fail("A ValueError was expected.")

        self.assertDictEqual(
            sb.__dict__,
            {
                **start_state,
                "_cells": {
                    (1, 2): 6,
                },
            }
        )
        
    def test_set_cell_8(self):
        sb = SudokuBoard()

        start_state = copy.deepcopy(sb.__dict__)

        try:
            sb.set_cell(1, 2, sb._max_val_value + 1)

        except ValueError as exception:
            self.assertEqual(
                str(exception),
                "The 'value' value %s is not an int in the range [%s, %s]"
                % (str(sb._max_val_value + 1), str(sb._min_val_value), str(sb._max_val_value))
            )

        else:
            self.fail("A ValueError was expected.")

        self.assertDictEqual(
            sb.__dict__,
            start_state
        )

    def test_set_cell_9(self):
        sb = SudokuBoard()

        start_state = copy.deepcopy(sb.__dict__)

        sb.set_cell(1, 2, 6)

        try:
            sb.set_cell(1, 2, sb._max_val_value + 1)

        except ValueError as exception:
            self.assertEqual(
                str(exception),
                "The 'value' value %s is not an int in the range [%s, %s]"
                % (str(sb._max_val_value + 1), str(sb._min_val_value), str(sb._max_val_value))
            )

        else:
            self.fail("A ValueError was expected.")

        self.assertDictEqual(
            sb.__dict__,
            {
                **start_state,
                "_cells": {
                    (1, 2): 6,
                },
            }
        )

    def test_set_cell_10(self):
        sb = SudokuBoard()

        start_state = copy.deepcopy(sb.__dict__)

        sb.set_cell(sb._min_row_value, sb._min_col_value, sb._min_val_value)
        sb.set_cell(sb._max_row_value, sb._max_col_value, sb._max_val_value)

        self.assertDictEqual(
            sb.__dict__,
            {
                **start_state,
                "_cells": {
                    (sb._min_row_value, sb._min_col_value): sb._min_val_value,
                    (sb._max_row_value, sb._max_col_value): sb._max_val_value,
                },
            }
        )

    def test_set_cell_11(self):
        sb = SudokuBoard()

        start_state = copy.deepcopy(sb.__dict__)

        try:
            sb.set_cell(1.1, 2, 3)

        except ValueError as exception:
            self.assertEqual(
                str(exception),
                "The 'row' value %s is not an int in the range [%s, %s]"
                % (str(1.1), str(sb._min_row_value), str(sb._max_row_value))
            )

        else:
            self.fail("A ValueError was expected.")

        self.assertDictEqual(
            sb.__dict__,
            start_state
        )

    def test_set_cell_12(self):
        sb = SudokuBoard()

        start_state = copy.deepcopy(sb.__dict__)

        sb.set_cell(1, 2, 6)

        try:
            sb.set_cell(1.1, 2, 3)

        except ValueError as exception:
            self.assertEqual(
                str(exception),
                "The 'row' value %s is not an int in the range [%s, %s]"
                % (str(1.1), str(sb._min_row_value), str(sb._max_row_value))
            )

        else:
            self.fail("A ValueError was expected.")

        self.assertDictEqual(
            sb.__dict__,
            {
                **start_state,
                "_cells": {
                    (1, 2): 6,
                },
            }
        )

    def test_set_cell_13(self):
        sb = SudokuBoard()

        start_state = copy.deepcopy(sb.__dict__)

        try:
            sb.set_cell(1, 2.2, 3)

        except ValueError as exception:
            self.assertEqual(
                str(exception),
                "The 'column' value %s is not an int in the range [%s, %s]"
                % (str(2.2), str(sb._min_col_value), str(sb._max_col_value))
            )

        else:
            self.fail("A ValueError was expected.")

        self.assertDictEqual(
            sb.__dict__,
            start_state
        )

    def test_set_cell_14(self):
        sb = SudokuBoard()

        start_state = copy.deepcopy(sb.__dict__)

        sb.set_cell(1, 2, 6)

        try:
            sb.set_cell(1, 2.2, 3)

        except ValueError as exception:
            self.assertEqual(
                str(exception),
                "The 'column' value %s is not an int in the range [%s, %s]"
                % (str(2.2), str(sb._min_col_value), str(sb._max_col_value))
            )

        else:
            self.fail("A ValueError was expected.")

        self.assertDictEqual(
            sb.__dict__,
            {
                **start_state,
                "_cells": {
                    (1, 2): 6,
                },
            }
        )

    def test_set_cell_15(self):
        sb = SudokuBoard()

        start_state = copy.deepcopy(sb.__dict__)

        try:
            sb.set_cell(1, 2, 3.3)

        except ValueError as exception:
            self.assertEqual(
                str(exception),
                "The 'value' value %s is not an int in the range [%s, %s]"
                % (str(3.3), str(sb._min_val_value), str(sb._max_val_value))
            )

        else:
            self.fail("A ValueError was expected.")

        self.assertDictEqual(
            sb.__dict__,
            start_state
        )

    def test_set_cell_16(self):
        sb = SudokuBoard()

        start_state = copy.deepcopy(sb.__dict__)

        sb.set_cell(1, 2, 6)

        try:
            sb.set_cell(1, 2, 3.3)

        except ValueError as exception:
            self.assertEqual(
                str(exception),
                "The 'value' value %s is not an int in the range [%s, %s]"
                % (str(3.3), str(sb._min_val_value), str(sb._max_val_value))
            )

        else:
            self.fail("A ValueError was expected.")

        self.assertDictEqual(
            sb.__dict__,
            {
                **start_state,
                "_cells": {
                    (1, 2): 6,
                },
            }
        )


class TestSudokuBoardRemoveCell(unittest.TestCase):

    def test_remove_cell_1(self):
        sb = SudokuBoard()

        sb.set_cell(1, 2, 3)

        start_state = copy.deepcopy(sb.__dict__)

        self.assertEqual(
            sb.remove_cell(1, 2),
            3
        )

        self.assertDictEqual(
            sb.__dict__,
            {
                **start_state,
                "_cells": {}
            }
        )

    def test_remove_cell_2(self):
        sb = SudokuBoard()

        sb.set_cell(1, 2, 3)

        start_state = copy.deepcopy(sb.__dict__)

        self.assertIsNone(
            sb.remove_cell(1, 3)
        )

        self.assertDictEqual(
            sb.__dict__,
            start_state
        )

    def test_remove_cell_3(self):
        sb = SudokuBoard()

        start_state = copy.deepcopy(sb.__dict__)

        self.assertIsNone(
            sb.remove_cell(1, 3)
        )

        self.assertDictEqual(
            sb.__dict__,
            start_state
        )

    def test_remove_cell_4(self):
        sb = SudokuBoard()

        start_state = copy.deepcopy(sb.__dict__)

        self.assertIsNone(
            sb.remove_cell(1, 3.3)
        )

        self.assertDictEqual(
            sb.__dict__,
            start_state
        )

    def test_remove_cell_5(self):
        sb = SudokuBoard()

        start_state = copy.deepcopy(sb.__dict__)

        self.assertIsNone(
            sb.remove_cell("hello", 3)
        )

        self.assertDictEqual(
            sb.__dict__,
            start_state
        )


class TestSudokuBoardRemoveAllCells(unittest.TestCase):

    def test_remove_all_cells_1(self):
        sb = SudokuBoard()

        sb.set_cell(1, 2, 3)

        start_state = copy.deepcopy(sb.__dict__)

        self.assertIsNone(
            sb.remove_all_cells()
        )

        self.assertDictEqual(
            sb.__dict__,
            {
                **start_state,
                "_cells": {}
            }
        )

    def test_remove_all_cells_2(self):
        sb = SudokuBoard()

        sb.set_cell(1, 2, 3)
        sb.set_cell(1, 3, 4)
        sb.set_cell(3, 5, 3)

        start_state = copy.deepcopy(sb.__dict__)

        self.assertIsNone(
            sb.remove_all_cells()
        )

        self.assertDictEqual(
            sb.__dict__,
            {
                **start_state,
                "_cells": {}
            }
        )

    def test_remove_all_cells_3(self):
        sb = SudokuBoard()

        start_state = copy.deepcopy(sb.__dict__)

        self.assertIsNone(
            sb.remove_all_cells()
        )

        self.assertDictEqual(
            sb.__dict__,
            {
                **start_state,
                "_cells": {}
            }
        )


class TestSudokuBoardGetCell(unittest.TestCase):

    def test_get_cell_1(self):
        sb = SudokuBoard()

        sb.set_cell(1, 2, 3)

        start_state = copy.deepcopy(sb.__dict__)

        self.assertEqual(
            sb.get_cell(1, 2),
            3
        )

        self.assertDictEqual(
            sb.__dict__,
            start_state
        )

    def test_get_cell_2(self):
        sb = SudokuBoard()

        sb.set_cell(1, 2, 3)
        sb.set_cell(1, 2, 4)
        sb.set_cell(1, 1, 5)

        start_state = copy.deepcopy(sb.__dict__)

        self.assertEqual(
            sb.get_cell(1, 2),
            4
        )

        self.assertDictEqual(
            sb.__dict__,
            start_state
        )

    def test_get_cell_3(self):
        sb = SudokuBoard()

        sb.set_cell(1, 2, 3)
        sb.set_cell(1, 2, 4)
        sb.set_cell(1, 1, 5)

        start_state = copy.deepcopy(sb.__dict__)

        self.assertIsNone(
            sb.get_cell(1, 6)
        )

        self.assertDictEqual(
            sb.__dict__,
            start_state
        )

    def test_get_cell_4(self):
        sb = SudokuBoard()

        start_state = copy.deepcopy(sb.__dict__)

        self.assertIsNone(
            sb.get_cell(1, 2)
        )

        self.assertDictEqual(
            sb.__dict__,
            start_state
        )

    def test_get_cell_5(self):
        sb = SudokuBoard()

        sb.set_cell(sb._max_row_value, sb._max_col_value, sb._max_val_value)
        sb.set_cell(1, 2, 4)
        sb.set_cell(1, 1, 5)

        start_state = copy.deepcopy(sb.__dict__)

        self.assertEqual(
            sb.get_cell(sb._max_row_value, sb._max_col_value),
            sb._max_val_value
        )

        self.assertDictEqual(
            sb.__dict__,
            start_state
        )

    def test_get_cell_6(self):
        sb = SudokuBoard()

        sb.set_cell(sb._min_row_value, sb._min_col_value, sb._min_val_value)
        sb.set_cell(1, 2, 4)
        sb.set_cell(1, 3, 5)

        start_state = copy.deepcopy(sb.__dict__)

        self.assertEqual(
            sb.get_cell(sb._min_row_value, sb._min_col_value),
            sb._min_val_value
        )

        self.assertDictEqual(
            sb.__dict__,
            start_state
        )


class TestSudokuBoardGetCells(unittest.TestCase):

    def test_get_cells_1(self):
        sb = SudokuBoard()

        start_state = copy.deepcopy(sb.__dict__)

        cells = sb.get_cells()

        self.assertDictEqual(cells, sb._cells)

        self.assertIsNot(cells, sb._cells)

        self.assertDictEqual(
            sb.__dict__,
            start_state
        )

    def test_get_cells_2(self):
        sb = SudokuBoard()

        sb.set_cell(1, 2, 3)

        start_state = copy.deepcopy(sb.__dict__)

        cells = sb.get_cells()

        self.assertDictEqual(cells, sb._cells)

        self.assertIsNot(cells, sb._cells)

        self.assertDictEqual(
            sb.__dict__,
            start_state
        )

    def test_get_cells_3(self):
        sb = SudokuBoard()

        sb.set_cell(1, 2, 3)
        sb.set_cell(sb._min_row_value, sb._min_col_value, sb._min_val_value)
        sb.set_cell(sb._max_row_value, sb._max_col_value, sb._max_val_value)

        start_state = copy.deepcopy(sb.__dict__)

        cells = sb.get_cells()

        self.assertDictEqual(cells, sb._cells)

        self.assertIsNot(cells, sb._cells)

        self.assertDictEqual(
            sb.__dict__,
            start_state
        )
