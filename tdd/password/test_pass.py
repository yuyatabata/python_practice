import unittest
from password import Calculator


class Calculate_number_of_password_types(unittest.TestCase):
    # def test(self):
    #     self.fail("空実装")

    def test_output_1_when_1_is_input(self):
        calculator = Calculator()
        self.assertEqual(1, calculator.calculate_permutation(1))

    def test_output_8_when_2_is_input(self):
        calculator = Calculator()
        self.assertEqual(8, calculator.calculate_permutation(2))


if __name__ == "__main__":
    unittest.main()
