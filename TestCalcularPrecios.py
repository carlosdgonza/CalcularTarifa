from datetime import *
import calendar
import sys
import unittest


formato = "%d/%m/%Y-%H:%M"

class tarifa:
    dias_semana = 0
    fines_semana = 0
    
class TestCalcularPrecios(unittest.TestCase):
    def testtimedelta15min(self):
        tarifa = Tarifa()
        tarifa.dias_semana = 1
        tarifa.fines_semana = 1
        
        ini = datetime.strptime("24/04/2016-20:15", formato)
        fin = datetime.strptime("24/04/2016-20:30", formato)

        self.assertEqual(1, calcularPrecio(tarifa, [ini, fin]))
        
if __name__ == "__main__":
    unittest.main()
        
        