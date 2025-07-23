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
        self.assertIn("Fizz - multiplo de 3", out)
        self.assertIn("3", out)

    def test_buzz(self):
        out = self.capturar_salida(6)
        self.assertIn("Buzz - multiplo de 5", out)
        self.assertIn("5", out)

    def test_fizzbuzz(self):
        out = self.capturar_salida(16)
        self.assertIn("FizzBuzz - multiplo de ambos", out)
        self.assertIn("15", out)


unittest.main()
