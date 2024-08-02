import unittest
from maxwell_equations import MaxwellEquations

class TestMaxwellEquations(unittest.TestCase):
    def setUp(self):
        self.maxwell = MaxwellEquations()
    
    def test_gauss_law_electric(self):
        self.assertTrue(self.maxwell.gauss_law_electric(10, 10))
        self.assertFalse(self.maxwell.gauss_law_electric(5, 10))  # Divergence does not match charge density
    
    def test_gauss_law_magnetic(self):
        self.assertTrue(self.maxwell.gauss_law_magnetic(0))
        self.assertFalse(self.maxwell.gauss_law_magnetic(5))  # Divergence of B field should be zero
    
    def test_faradays_law(self):
        self.assertTrue(self.maxwell.faradays_law(-3, 3))
        self.assertFalse(self.maxwell.faradays_law(2, -3))  # Curl of E and rate of change of B do not match
    
    def test_ampere_maxwell_law(self):
        self.assertTrue(self.maxwell.ampere_maxwell_law(4, 4))
        self.assertFalse(self.maxwell.ampere_maxwell_law(3, 5))  # Curl of B and current+displacement current do not match

if __name__ == '__main__':
    unittest.main()
