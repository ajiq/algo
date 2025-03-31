import unittest
from unittest.mock import patch
from io import StringIO
import calculator

class TestCalculator(unittest.TestCase):
    @patch('builtins.input', side_effect=['3', '7'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_positive_numbers(self, mock_stdout, mock_input):
        calculator.calculate_sum()
        self.assertEqual(mock_stdout.getvalue().strip(), "Результат: 10")

    @patch('builtins.input', side_effect=['5', '-3'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_mixed_numbers(self, mock_stdout, mock_input):
        calculator.calculate_sum()
        self.assertEqual(mock_stdout.getvalue().strip(), "Результат: 2")

if __name__ == "__main__":
    unittest.main()
