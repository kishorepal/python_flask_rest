import unittest
from main.common.utility_functions import UtiliyFunctions



class TestUtilityFunctions(unittest.TestCase):
    utilityFunction = None
    
    def test_get_name(self):
        utilityFunction = UtiliyFunctions.getInstance()
        name = utilityFunction.getName()
        print name
        
    

if __name__ == "__main__":
    unittest.main()

