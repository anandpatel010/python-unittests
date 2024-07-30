import unittest
from temperature_converter import TemperatureConverter

class TestTemperatureConverter(unittest.TestCase):
    def setUp(self):
        self.converter = TemperatureConverter()
    
    def test_celsius_to_fahrenheit(self):
        result = self.converter.celsius_to_fahrenheit(0)
        self.assertEqual(result, 32.0)
        result = self.converter.celsius_to_fahrenheit(100)
        self.assertEqual(result, 212.0)
    
    def test_fahrenheit_to_celsius(self):
        result = self.converter.fahrenheit_to_celsius(32)
        self.assertEqual(result, 0.0)
        result = self.converter.fahrenheit_to_celsius(212)
        self.assertEqual(result, 100.0)
    
    def test_conversion_accuracy(self):
        # Testing some random values for accuracy
        self.assertAlmostEqual(self.converter.celsius_to_fahrenheit(37), 98.6)
        self.assertAlmostEqual(self.converter.fahrenheit_to_celsius(98.6), 37)

if __name__ == '__main__':
    unittest.main()

