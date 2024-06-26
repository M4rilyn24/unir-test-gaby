import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))

    def test_subtract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.subtract(2, 2))
        self.assertEqual(4, self.calc.subtract(6, 2))
        self.assertEqual(-4, self.calc.subtract(2, 6))

    def test_multiply_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))

    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_square_root_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.square_root(4))
        self.assertEqual(3, self.calc.square_root(9))
        self.assertRaises(ValueError, self.calc.square_root, -4)

    def test_log_base_10_method_returns_correct_result(self):
        self.assertAlmostEqual(1, self.calc.log_base_10(10))
        self.assertAlmostEqual(2, self.calc.log_base_10(100))
        self.assertRaises(ValueError, self.calc.log_base_10, -10)
        self.assertRaises(ValueError, self.calc.log_base_10, 0)

    def test_add_method_fails_with_invalid_parameters(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    def test_divide_method_fails_with_invalid_parameters(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(ValueError, self.calc.divide, 2, 0)
        self.assertRaises(ValueError, self.calc.divide, 2, -0)
        self.assertRaises(ValueError, self.calc.divide, 0, 0)
        self.assertRaises(ValueError, self.calc.divide, "0", 0)

    @patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_calls_validate_permissions(self, _validate_permissions):
        self.calc.multiply(2, 2)
        _validate_permissions.assert_called_with('2 * 2', 'user1')


if __name__ == "__main__":
    unittest.main()
