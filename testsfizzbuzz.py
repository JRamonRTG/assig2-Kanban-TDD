import unittest
from io import StringIO
from contextlib import redirect_stdout
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    def capturar_salida(self, n):
        buffer = StringIO()
        with redirect_stdout(buffer):
            fizzbuzz(n)
        return buffer.getvalue()
    
    def test_fizz(self):
        out = self.capturar_salida(4)
        self.assertIn("Fizz", out)
        self.assertIn("3", out)

unittest.main()
