import unittest
from employee import Employee

class employee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass\n")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        print("Setup")
        self.emp_1 = Employee("Hareesh", "Duddupudi", 90000)
        self.emp_2 = Employee("Venky", "Mogalappu", 80000)

    def tearDown(self):
        print("tearDown \n")

    def test_email(self):
        print("test_email")
        self.assertEqual(self.emp_1.email(), "Hareesh.Duddupudi@gmail.com")
        self.assertEqual(self.emp_2.email(), "Venky.Mogalappu@gmail.com")

        self.emp_1.first = "Rajesh"
        self.emp_2.first = "Vishali"

        self.assertEqual(self.emp_1.email(), "Rajesh.Duddupudi@gmail.com")
        self.assertEqual(self.emp_2.email(), "Vishali.Mogalappu@gmail.com")

    def test_name(self):
        print("test_name")
        self.assertEqual(self.emp_1.fullname(), "Hareesh Duddupudi")
        self.assertEqual(self.emp_2.fullname(), "Venky Mogalappu")

        self.emp_1.first = "Rajesh"
        self.emp_2.first = "Vishali"

        self.assertEqual(self.emp_1.fullname(), "Rajesh Duddupudi")
        self.assertEqual(self.emp_2.fullname(), "Vishali Mogalappu")

    def test_apply_raise(self):
        print("test_apply_raise")

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 90000 * Employee.raise_amt)
        self.assertEqual(self.emp_2.pay, 80000 * Employee.raise_amt)

if __name__ == "__main__":
    unittest.main()
