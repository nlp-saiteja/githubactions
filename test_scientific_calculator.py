import unittest
from scientific_calculator import *

class TestScientificCalculator(unittest.TestCase):
#Testing Sin Function
    def test_sin_positive_input(self):
        self.assertEqual(sin(90), 1.0)
    
    def test_sin_negative_input(self):
        self.assertEqual(sin(-90), -1.0)
    
    def test_sin_zero_input(self):
        self.assertEqual(sin(0), 0.0)
    
    def test_sin_non_numeric_input(self):
        with self.assertRaises(TypeError):
            sin("hello")
        
#Testing Cos Function
    def test_cos_positive_input(self):
         self.assertEqual(round(cos(60),1), 0.5)

    def test_cos_negative_input(self):
         self.assertEqual(round(cos(-120),1), -0.5)

    def test_cos_zero_input(self):
         self.assertEqual(round(cos(0),1), 1.0)
         
    def test_cos_non_numeric_input(self):
        with self.assertRaises(TypeError):
            cos("PSD")

#Testing Tan Function
    def test_tan_positive_input(self):          
         self.assertEqual(round(tan(45),1), 1.0)

    def test_tan_negative_input(self):
         self.assertEqual(round(tan(-45),1), -1.0)

    def test_tan_zero_input(self):
         self.assertEqual(tan(0), 0.0)

    def test_tan_non_numeric_input(self):
        with self.assertRaises(TypeError):
            tan("Impulse")
    
#Testing sqrt Function
    def test_sqrt_positive_input(self):
         self.assertEqual(sqrt(4), 2.0)

    def test_sqrt_negative_input(self):
         with self.assertRaises(ValueError):
            sqrt(-4)

    def test_sqrt_non_numeric_input(self):
        with self.assertRaises(TypeError):
            sqrt("Magic")

#Testing log Function
    def test_log_positive_input(self):  
         self.assertEqual(log(10,10), 1)

    def test_log_negative_input(self):
        with self.assertRaises(ValueError):
            log(-1,10)

    def test_log_non_numeric_input(self):
        with self.assertRaises(TypeError):
            log("Infinity",10)

#Testing asin Function
    def test_asin(self):
        self.assertEqual(round(asin(0), 5), round(0, 5))
        self.assertEqual(round(asin(1), 5), round(math.pi/2, 5))
        self.assertEqual(round(asin(-1), 5), round(-math.pi/2, 5))

#Testing acos Function
    def test_acos(self):
        self.assertEqual(round(acos(0), 5), round(math.pi/2, 5))
        self.assertEqual(round(acos(1), 5), round(0, 5))
        self.assertEqual(round(acos(-1), 5), round(math.pi, 5))

#Testing atan Function
    def test_atan(self):
        self.assertEqual(round(atan(0), 5), round(0, 5))
        self.assertEqual(round(atan(1), 5), round(math.pi/4, 5))
        self.assertEqual(round(atan(-1), 5), round(-math.pi/4, 5))

#Testing sinh Function
    def test_sinh(self):
        self.assertEqual(round(sinh(0), 5), round(0, 5))
        self.assertEqual(round(sinh(1), 5), round(math.sinh(1), 5))

#Testing cosh Function
    def test_cosh(self):
        self.assertEqual(round(cosh(0), 5), round(1, 5))
        self.assertEqual(round(cosh(1), 5), round(math.cosh(1), 5))

#Testing tanh Function
    def test_tanh(self):
        self.assertEqual(round(tanh(0), 5), round(0, 5))
        self.assertEqual(round(tanh(1), 5), round(math.tanh(1), 5))

if __name__ == '__main__':
    unittest.main()


