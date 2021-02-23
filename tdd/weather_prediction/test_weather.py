import unittest
from weather import Predict_Weather


class Predict_weather_for_next_day(unittest.TestCase):
    def test_cloudy_after_sunny(self):
        # self.fail("空実装")
        predict_weather = Predict_Weather()
        self.assertEqual("Cloudy", predict_weather.predict("Sunny"))

    def test_rainny_after_cloudy(self):
        predict_weather = Predict_Weather()
        self.assertEqual("Rainy", predict_weather.predict("Cloudy"))

    def test_sunny_after_rainny(self):
        predict_weather = Predict_Weather()
        self.assertEqual("Sunny", predict_weather.predict("Rainy"))


if __name__ == "__main__":
    unittest.main()
