'''
Created on Apr 25, 2016
@author: carlos
'''

from datetime import *
import calendar
import sys
 
dicdias = {'MONDAY':'Lunes','TUESDAY':'Martes','WEDNESDAY':'Miercoles','THURSDAY':'Jueves', \
'FRIDAY':'Viernes','SATURDAY':'Sabado','SUNDAY':'Domingo'}


formato = "%d/%m/%Y-%H:%M"

class tarifa:
    dias_semana = 0
    fines_semana = 0
    

def calcularPrecio(tarifa, tiempoTrabajo):
    
    aux = 0
    contador = tiempoTrabajo[0]
    tarifaTotal = 0
    
    while  (contador < tiempoTrabajo[1] and aux < 168):
        if (tiempoTrabajo[1] - tiempoTrabajo[0] < timedelta(minutes=15)):
            tarifaTotal = 0
            break
        
        
        
        a = dicdias[contador.strftime('%A').upper()]
        #print(a)
        if  (a == 'Lunes' or a == 'Martes' or a == 'Miercoles' or a == 'Jueves' or a == 'Viernes'):
            tarifaTotal = tarifaTotal + tarifa.dias_semana 
        
            
        elif (a == 'Sabado' or a == 'Domingo'):
            tarifaTotal = tarifaTotal + tarifa.fines_semana
            
        
        contador = contador + timedelta(hours=1)
        aux = aux+1
        
    return tarifaTotal
<<<<<<< HEAD


=======
>>>>>>> CasosInvalidosValen
    