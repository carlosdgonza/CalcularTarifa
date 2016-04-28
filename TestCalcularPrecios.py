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
    def testtimedelta15min(self):
        
        tarifa.dias_semana = 1
        tarifa.fines_semana = 1
        
        ini = datetime.strptime("24/04/2016-20:15", formato)
        fin = datetime.strptime("24/04/2016-20:30", formato)

        self.assertEqual(1, calcularPrecio(tarifa, [ini, fin]))
        
        
    def testtimedelta7dias(self):
        
        tarifa.dias_semana = 1
        tarifa.fines_semana = 1
        
        ini = datetime.strptime("24/04/2016-20:15", formato)
        fin = datetime.strptime("01/05/2016-20:15", formato)

        self.assertEqual(168, calcularPrecio(tarifa, [ini, fin]))
        
    def testtimedelta1hora1min(self):
        
        tarifa.dias_semana = 1
        tarifa.fines_semana = 1
        
        ini = datetime.strptime("24/04/2016-20:15", formato)
        fin = datetime.strptime("24/04/2016-21:16", formato)

        self.assertEqual(2, calcularPrecio(tarifa, [ini, fin]))
        
    def testequalstimes(self):
        
        tarifa.dias_semana = 1
        tarifa.fines_semana = 1
        
        ini = datetime.strptime("24/04/2016-20:15", formato)
        fin = datetime.strptime("24/04/2016-20:15", formato)

        self.assertEqual(0, calcularPrecio(tarifa, [ini, fin]))
        
    
    def testtimedeltamas7dias(self):
        
        tarifa.dias_semana = 1
        tarifa.fines_semana = 1
        
        ini = datetime.strptime("24/04/2016-20:15", formato)
        fin = datetime.strptime("05/05/2016-21:15", formato)

        self.assertEqual(168, calcularPrecio(tarifa, [ini, fin]))    
        
    def testtarifasem0(self):
        
        tarifa.dias_semana = 0
        tarifa.fines_semana = 1
        
        ini = datetime.strptime("25/04/2016-20:15", formato)
        fin = datetime.strptime("30/04/2016-20:15", formato)

        self.assertEqual(20, calcularPrecio(tarifa, [ini, fin]))    
        
    def testtarifafines0(self):
        
        tarifa.dias_semana = 1
        tarifa.fines_semana = 0
        
        ini = datetime.strptime("25/04/2016-20:15", formato)
        fin = datetime.strptime("30/04/2016-20:15", formato)

        self.assertEqual(100, calcularPrecio(tarifa, [ini, fin]))    
        
if __name__ == "__main__":
    unittest.main()
        
        