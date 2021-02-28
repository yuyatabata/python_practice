import unittest
from red import Red_or_not


class Check_a_is_over_2800_and_less_than_5000(unittest.TestCase):
    # def test_empty_implement(self):
    #     self.fail('空実装')

    def test_output_false_when_a_is_5000(self):
        red_or_not = Red_or_not()
        self.assertEqual(False, red_or_not.check_validity_input_a(5000))

    def test_output_false_when_a_is_2799(self):
        red_or_not = Red_or_not()
        self.assertEqual(False, red_or_not.check_validity_input_a(2799))


class Output_s_if_a_is_over_3200_else_red(unittest.TestCase):
    def test_output_s_when_3200_is_input(self):
        red_or_not = Red_or_not()
        self.assertEqual(
            'pink', red_or_not.compare_with_standard_value(3200, 'pink'))

    def test_output_red_when_3199_is_input(self):
        red_or_not = Red_or_not()
        self.assertEqual(
            'red', red_or_not.compare_with_standard_value(3199, 'pink'))


if __name__ == "__main__":
    unittest.main()
