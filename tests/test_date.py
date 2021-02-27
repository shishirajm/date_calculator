import unittest
from datetime import datetime

from parameterized import parameterized

from date_calculator.date import Date


def func():
    raise Exception('lets see if this works')


class MyTestCase(unittest.TestCase):
    def test_date_diff_should_be_valid(self):
        d1 = datetime.strptime("03/02/2020", "%d/%m/%Y")
        d2 = datetime.strptime("01/03/2020", "%d/%m/%Y")
        print(d1.day)
        days = abs((d2 - d1).days)
        print(days)
        self.assertEqual(True, True)

    def test_date_instance_should_be_valid(self):
        s = '01/02/2021'
        d = Date(s)
        print(d.day, d.month, d.year)
        self.assertEqual(d.day, 1)
        self.assertEqual(d.month, 2)
        self.assertEqual(d.year, 2021)

    def test_date_instance_with_wrong_date_should_raise_exception_2(self):
        self.assertRaises(Exception, lambda: Date('31/04/2021'))

    @parameterized.expand([
        '0/01/2021',
        '32/01/2021',
        '31/04/2021',
        '50/05/2021',
        '-1/06/2021',
    ])
    def test_date_instance_with_wrong_date_should_raise_exception(self, d):
        print(d)
        self.assertRaises(Exception, lambda: Date(d))

    @parameterized.expand([
        '01/13/2021',
        '01/0/2021'
    ])
    def test_date_instance_with_wrong_month_should_raise_exception(self, d):
        self.assertRaises(Exception, lambda: Date(d))



if __name__ == '__main__':
    unittest.main()
