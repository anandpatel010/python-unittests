import unittest
from shape_calculator import ShapeCalculator

class TestShapeCalculator(unittest.TestCase):
    def test_rectangle_area(self):
        calc = ShapeCalculator()
        result = calc.rectangle_area(5, 3)
        self.assertEqual(result, 15)

    def test_circle_area(self):
        calc = ShapeCalculator()
        result = calc.circle_area(2)
        self.assertAlmostEqual(result, 12.566370614359172)  # π * r^2 ≈ 12.566

if __name__ == '__main__':
    unittest.main()

