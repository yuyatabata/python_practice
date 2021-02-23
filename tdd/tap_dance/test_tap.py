import unittest
from tap import Check_ease_of_step


class Check_if_the_string_is_easy_to_tap(unittest.TestCase):
    # def test_print_no_when_odd_character_is_not_in_RUD(self):
    #     # self.fail("空実装")
    #     check_ease_of_step = Check_ease_of_step()
    #     self.assertEqual('No', check_ease_of_step.check_string('DULL'))

    def test_print_no_when_odd_character_is_not_in_RUD(self):
        check_ease_of_step = Check_ease_of_step()
        self.assertEqual(
            "No", check_ease_of_step.check_string("DULL"))

    def test_print_no_when_even_character_is_not_in_RUD(self):
        check_ease_of_step = Check_ease_of_step()
        self.assertEqual(
            "No", check_ease_of_step.check_string("ULURU"))

    def test_print_when_even_character_is_in_RUD(self):
        check_ease_of_step = Check_ease_of_step()
        self.assertEqual(
            "Yes", check_ease_of_step.check_string("RDULULDURURLRDULRLR"))


if __name__ == "__main__":
    unittest.main()
