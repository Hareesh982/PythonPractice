import unittest
import calc

class test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(3, 5), 8)
        self.assertEqual(calc.add(-3, -5), -8)
        self.assertEqual(calc.add(3, -5), -2)
        self.assertEqual(calc.add(-3, 5), 2)
    
    def test_sub(self):
        self.assertEqual(calc.sub(3, 5), -2)
        self.assertEqual(calc.sub(-3, -5), 2)
        self.assertEqual(calc.sub(3, -5), 8)
        self.assertEqual(calc.sub(-3, 5), -8)

    def test_multi(self):
        self.assertEqual(calc.multi(3, 5), 15)
        self.assertEqual(calc.multi(-3, -5), 15)
        self.assertEqual(calc.multi(3, -5), -15)
        self.assertEqual(calc.multi(-3, 5), -15)
        self.assertEqual(calc.multi(0, 5), 0)

    def test_div(self):
        self.assertEqual(calc.div(3, 5), 0.6)
        self.assertEqual(calc.div(-3, -5), 0.6)
        self.assertEqual(calc.div(3, -5), -0.6)
        self.assertEqual(calc.div(-3, 5), -0.6)
        with self.assertRaises(ValueError):
            calc.div(10,0)

if __name__ == "__main__":
    unittest.main()