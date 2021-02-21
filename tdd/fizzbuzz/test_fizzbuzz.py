import unittest
from fizzbuzz import FizzBuzz


class Output_Fizz_when_multiple_of_3_is_input(unittest.TestCase):
    # def test(self):
    #     self.fail("必ず失敗")

    def test_output_fizz_when_3_is_input(self):
        fizzbuzz = FizzBuzz()
        self.assertEqual('Fizz', fizzbuzz.convert(3))

    # 三角測量
    # def test_output_fizz_when_6_is_input(self):
    #     fizzbuzz = FizzBuzz()
    #     self.assertEqual('Fizz', fizzbuzz.convert(6))


class Output_Fizz_when_multiple_of_5_is_input(unittest.TestCase):

    # 明白な実装
    def test_output_fizz_when_5_is_input(self):
        fizzbuzz = FizzBuzz()
        self.assertEqual('Buzz', fizzbuzz.convert(5))


class Output_FizzBuzz_for_multiples_of_both_3_and_5(unittest.TestCase):
    def test_output_fizzbuzz_when_15_is_input(self):
        fizzbuzz = FizzBuzz()
        self.assertEqual('FizzBuzz', fizzbuzz.convert(15))

    def test_output_fizzbuzz_when_30_is_input(self):
        fizzbuzz = FizzBuzz()
        self.assertEqual('FizzBuzz', fizzbuzz.convert(30))


if __name__ == "__main__":
    unittest.main()
