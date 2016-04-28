from datetime import *
import calendar
import sys
import unittest

class TestCalcularPrecios(unittest.TestCase):
    def testtimedelta15min(self):
        tarifa = Tarifa()
        tarifa.dias_semana = 1
        tarifa.fines_semana = 1
        ini = datetime.datetime(2016, 4, 1, 7, 0)
        fin = datetime.datetime(2016, 4, 1, 7, 15)

        self.assertEqual(1, calcularPrecio(tarifa, [ini, fin]))
        
if __name__ == "__main__":
    unittest.main()
        
        