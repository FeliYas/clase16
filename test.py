import unittest
from calculadora import Calculadora
from cadenatxt import check_text

calc = Calculadora()

class Test(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(calc.sum(1,2),3)
    def test_rest(self):
        self.assertEqual(calc.rest(1,2),-1)
    def test_multi(self):
        self.assertEqual(calc.mult(1,2),2)
    def test_div(self):
        self.assertEqual(calc.div(1,2),0.5)
      
    def test_check_text(self):
        self.assertEqual(check_text("Hola"),"Hola")
    def test_check_text_2(self):
        self.assertEqual(check_text("hola"),"hola")

  
if __name__ == '__main__':
    unittest.main()