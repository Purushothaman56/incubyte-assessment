import unittest
from sum_string_numbers import add

class TestAddFunction(unittest.TestCase):

    def test_no_input(self):
        result = add()
        self.assertEqual(result, 0)

    def test_empty_input(self):
        result = add("")
        self.assertEqual(result, 0)

    def test_input_contains_only_spaces(self):
        space_result = add("  ")
        tab_result = add("\t\t")
        new_line_result = add("\n\n")
        all_spaces = add(" \n\t")
        self.assertEqual(space_result, 0)
        self.assertEqual(tab_result, 0)
        self.assertEqual(new_line_result, 0)
        self.assertEqual(all_spaces, 0)

    def test_input_single_digit_zero(self):
        result = add("0")
        self.assertEqual(result, 0)

    def test_input_single_digit_one(self):
        result = add("1")
        self.assertEqual(result, 1)

    def test_input_single_digit_nintynine(self):
        result = add("99")
        self.assertEqual(result, 99)

    def test_input_single_digit_nintynine_plus_hundred(self):
        result = add("99,100")
        self.assertEqual(result, 199)

if __name__ == "__main__":
    unittest.main()
