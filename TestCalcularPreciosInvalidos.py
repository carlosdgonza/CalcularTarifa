from datetime import *
import calendar
import sys
import unittest
from CalcularPrecio import *

formato = "%d/%m/%Y-%H:%M"

class tarifa:
    dias_semana = 0
    fines_semana = 0
    
tarifa = tarifa()
    
class TestCalcularPrecios(unittest.TestCase):
    def testtarifaSemNeg(self):
        tarifa.dias_semana = -1
        tarifa.fines_semana = 1
        
        
        ini = datetime.strptime("25/04/2016-20:15", formato)
        fin = datetime.strptime("25/04/2016-20:30", formato)

        self.assertEqual(-1, calcularPrecio(tarifa, [ini, fin]))
        
    def testtarifaFinNeg(self):
        tarifa.dias_semana = 1
        tarifa.fines_semana =-1
        
        
        ini = datetime.strptime("24/04/2016-20:15", formato)
        fin = datetime.strptime("24/04/2016-20:30", formato)

        self.assertEqual(-1, calcularPrecio(tarifa, [ini, fin]))
        
    def testTiempoFinalMenor(self):
        tarifa.dias_semana = 1
        tarifa.fines_semana = 1
        
        
        ini = datetime.strptime("24/04/2016-20:15", formato)
        fin = datetime.strptime("13/04/2016-20:30", formato)

        self.assertEqual(0, calcularPrecio(tarifa, [ini, fin]))
        
        
if __name__ == "__main__":
    unittest.main()
        
        