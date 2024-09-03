import unittest
from sum_string_numbers import add

class TestAddFunction(unittest.TestCase):

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

    def test_input_multiple_digits(self):
        all_different_result = add("0,,,1,2,3,4,,5,6,7,8,9,10")
        all_same_result = add("1,,1,1,,1,1,1,1,1,1,1,,,,")
        all_zeros = add("0,0,0,0,0,0,0,0,0,0,0,0,0,,0,,,0,")
        self.assertEqual(all_different_result, 55)
        self.assertEqual(all_same_result, 10)
        self.assertEqual(all_zeros, 0)

    def test_input_with_new_line(self):
        result_1_with_new_line = add("1\n2,3")
        result_2_with_new_line = add("1,\n")
        self.assertEqual(result_1_with_new_line, 6)
        self.assertEqual(result_2_with_new_line, 1)

    def test_input_with_single_delimeter(self):
        result = add("//;\n1;2")
        self.assertEqual(result, 3)

    def test_input_with_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            add("//;\n1;2;-3;0;-6")
        self.assertEqual(str(context.exception), "Negatives not allowed: -3, -6")

    def test_input_single_negative(self):
        with self.assertRaises(ValueError) as context:
            add("-1")
        self.assertEqual(str(context.exception), "Negatives not allowed: -1")

    def test_input_all_negatives(self):
        with self.assertRaises(ValueError) as context:
            add("-100,-5,-10")
        self.assertEqual(str(context.exception), "Negatives not allowed: -100, -5, -10")

    def test_input_negatives_with_multiple_delimeters(self):
        with self.assertRaises(ValueError) as context:
            add("//[&][**]\n-100&-5**-10")
        self.assertEqual(str(context.exception), "Negatives not allowed: -100, -5, -10")

    def test_input_ignores_bigger_than_1000(self):
        result = add("//;\n1;2;1001;1000")
        self.assertEqual(result, 1003)

    def test_delimeters_length(self):
        result = add("//[***]\n1***2***3")
        self.assertEqual(result, 6)

    def test_multiple_delimeters(self):
        result = add("//[*][%]\n1*2%3")
        self.assertEqual(result, 6)

    def test_multiple_delimeters_upto_5(self):
        result = add("//[**][%%][|][:][_]\n1**2%%3|4:5_6")
        self.assertEqual(result, 21)

class TestOtherFactors(unittest.TestCase):

    def test_invalid_delimiter_format(self):
        with self.assertRaises(ValueError) as context:
            add("//[;[1;2")
        self.assertIn("Invalid input format: ", str(context.exception))

if __name__ == "__main__":
    unittest.main()
