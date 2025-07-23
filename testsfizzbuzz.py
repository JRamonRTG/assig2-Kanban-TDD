# testsfizzbuzz.py
# Pruebas unitarias para fizzbuzz usando unittest y redirect_stdout
# importaciones necesarias
import unittest
from io import StringIO
from contextlib import redirect_stdout
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):

    # Captura la salida de consola al ejecutar fizzbuzz(n)
    def capturar_salida(self, n):
        buffer = StringIO()
        with redirect_stdout(buffer):
            fizzbuzz(n)
        return buffer.getvalue()
    
    def test_fizz(self):
        # Prueba que el programa imprima "fizz"
        # Ejecutamos fizzbuzz(n) con n = 4
        # Esperamos que imprima "Buzz - multiplo de 3" para el numero 3
        out = self.capturar_salida(4)
        
        # Verificamos que la salida contiene el texto esperado para multiplos de 3
        self.assertIn("Fizz - multiplo de 3", out)

         # Tambien verificamos que el numero 3 fue efectivamente impreso
        self.assertIn("3", out)

    def test_buzz(self):
        out = self.capturar_salida(6)
        self.assertIn("Buzz - multiplo de 5", out)
        self.assertIn("5", out)

    def test_fizzbuzz(self):
        out = self.capturar_salida(16)
        self.assertIn("FizzBuzz - multiplo de ambos", out)
        self.assertIn("15", out)

# Ejecuta los tests

unittest.main()
