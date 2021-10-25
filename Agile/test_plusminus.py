import unittest
from plusminus import Diffadd

class testplusminus(unittest.TestCase):
    v1=Diffadd(5,3)
    
    def testPlus(self):
        self.assertAlmostEqual(v1.add(),8)
    
    def testMinus(self):
        self.assertAlmostEqual(v1.diff(),2)
        
        
