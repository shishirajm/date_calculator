import unittest
from datetime import datetime

from parameterized import parameterized

from src.date import Date


class TestDate(unittest.TestCase):
    @parameterized.expand([
        ('01/01/2021', 1, 1, 2021),
        ('01/01/01', 1, 1, 1),
        ('29/02/400', 29, 2, 400),
        ('29/02/2020', 29, 2, 2020),
        ('31/01/2021', 31, 1, 2021),
        ('30/04/2021', 30, 4, 2021),
        ('29/02/2000', 29, 2, 2000)
    ])
    def test_date_instance_should_be_valid(self, date, day, month, year):
        d = Date(date)
        self.assertEqual(d.day, day)
        self.assertEqual(d.month, month)
        self.assertEqual(d.year, year)

    def test_date_instance_with_wrong_date_format_should_raise_exception_2(self):
        self.assertRaises(Exception, lambda: Date('31/04/2021', 'MM/DD/YYYY'))

    def test_date_instance_with_text_date_should_raise_exception_2(self):
        self.assertRaises(Exception, lambda: Date('Some/Random/Text'))

    @parameterized.expand([
        '0/01/2021',
        '32/01/2021',
        '31/04/2021',
        '50/05/2021',
        '-1/06/2021',
        '29/02/1900',
        '29/02/200',
    ])
    def test_date_instance_with_wrong_day_should_raise_exception(self, d):
        self.assertRaises(Exception, lambda: Date(d))

    @parameterized.expand([
        '01/13/2021',
        '01/0/2021'
    ])
    def test_date_instance_with_wrong_month_should_raise_exception(self, d):
        self.assertRaises(Exception, lambda: Date(d))

    @parameterized.expand([
        '01/13/-1',
        '01/0/0'
    ])
    def test_date_instance_with_wrong_year_should_raise_exception(self, d):
        self.assertRaises(Exception, lambda: Date(d))

    @parameterized.expand([
        ('01/01/2000', '03/01/2000'),
        ('03/01/2000', '01/01/2000'),
        ('01/01/0001', '01/01/0002'),
        ('01/01/0001', '01/01/2021'),
        ('02/06/1983', '22/06/1983'),
        ('04/07/1984', '25/12/1984'),
        ('03/01/1989', '03/08/1983'),
        ('28/02/2000', '01/03/2000'),
    ])
    def test_date_diff_should_be_valid_for_different_dates(self, date1, date2):
        lib_d1 = datetime.strptime(date1, "%d/%m/%Y")
        lib_d2 = datetime.strptime(date2, "%d/%m/%Y")
        expected = abs((lib_d2 - lib_d1).days) - 1

        d1 = Date(date1)
        d2 = Date(date2)
        actual = d2 - d1

        self.assertEqual(expected, actual)

    @parameterized.expand([
        ('01/01/2000', '01/01/2000'),
        ('29/02/2020', '29/02/2020'),
    ])
    def test_date_diff_should_be_zero_for_same_date(self, date1, date2):
        d1 = Date(date1)
        d2 = Date(date2)
        actual = d2 - d1

        self.assertEqual(0, actual)


if __name__ == '__main__':
    unittest.main()
