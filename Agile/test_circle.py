import unittest
from circle import circlearea

class testcircle(unittest.TestCase):
    
    def test_Area_Positive(self):
        self.assertAlmostEqual(circlearea(1),3.14)
        self.assertAlmostEqual(circlearea(2),6.28)
        
    def test_Area_Negative(self):
        self.assertRaises(ValueError, circlearea,-5)
    
    
