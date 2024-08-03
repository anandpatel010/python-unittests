import unittest
from potential_energy_calculator import PotentialEnergyCalculator

class TestPotentialEnergyCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = PotentialEnergyCalculator()
    
    def test_gravitational_potential_energy(self):
        self.assertAlmostEqual(self.calculator.gravitational_potential_energy(10, 9.81, 5), 490.5)
        self.assertAlmostEqual(self.calculator.gravitational_potential_energy(2, 9.81, 10), 196.2)
        self.assertAlmostEqual(self.calculator.gravitational_potential_energy(0, 9.81, 10), 0)
    
    def test_elastic_potential_energy(self):
        self.assertAlmostEqual(self.calculator.elastic_potential_energy(100, 0.5), 12.5)
        self.assertAlmostEqual(self.calculator.elastic_potential_energy(200, 1), 100)
        self.assertAlmostEqual(self.calculator.elastic_potential_energy(50, 2), 100)
    
    def test_zero_displacement(self):
        self.assertAlmostEqual(self.calculator.elastic_potential_energy(50, 0), 0)

if __name__ == '__main__':
    unittest.main()
