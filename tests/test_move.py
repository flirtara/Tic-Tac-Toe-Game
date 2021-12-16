from unittest import TestCase
from move import Move


class MoveTest(TestCase):

    def test_create_move(self):
        my_move1 = Move(1)
        self.assertEqual(1, my_move1.value)

        my_move2 = Move(5)
        self.assertEqual(5, my_move2.value)

        my_move3 = Move(9)
        self.assertEqual(9, my_move3.value)

    def test_is_valid_move(self):
        my_move1 = Move(-1)
        self.assertEqual(False, my_move1.is_valid())

        my_move2 = Move(3)
        self.assertEqual(True, my_move2.is_valid())

        my_move2 = Move(10)
        self.assertEqual(False, my_move2.is_valid())

    def test_get_row(self):
        first_row = Move(2)
        self.assertEqual(0, first_row.get_row())

        second_row = Move(6)
        self.assertEqual(1, second_row.get_row())

        third_row = Move(7)
        self.assertEqual(2, third_row.get_row())

    def test_get_column(self):
        first_column = Move(1)
        self.assertEqual(0, first_column.get_column())

        second_column = Move(5)
        self.assertEqual(1, second_column.get_column())

        third_column = Move(9)
        self.assertEqual(2, third_column.get_column())
