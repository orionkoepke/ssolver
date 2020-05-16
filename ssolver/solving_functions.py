import os
import typing

from clyngor.inline import ASP_one_model
from .sudoku_board import SudokuBoard


def get_answer_set_program() -> str:
    cwd = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(cwd, "sudoku_solver.as"), "r") as file:
        answer_set_program = file.read()

    return answer_set_program


def convert_to_intput(board: SudokuBoard) -> str:
    answer_set_program = ""

    for position, value in board.get_cells().items():
        row, column = position
        answer_set_program += "sudoku(%d, %d, %d).\n" % (row, column, value)

    return answer_set_program


def solve(board: SudokuBoard) -> typing.Union[SudokuBoard, None]:
    answer_set_program = get_answer_set_program()
    answer_set_input = convert_to_intput(board)

    answer_set = ASP_one_model(answer_set_program + "\n" + answer_set_input)

    answer = SudokuBoard()
    for row, column, value in [values for name, values in answer_set]:
        answer.set_cell(row, column, value)

    return answer
