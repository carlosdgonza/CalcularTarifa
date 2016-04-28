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
    
    if (tiempoTrabajo[1] - tiempoTrabajo[0] < timedelta(minutes=15) or timedelta(days=7) < tiempoTrabajo[1] - tiempoTrabajo[0]):
    
        print("ERROR: El tiempo de trabajo no puede ser menor a 15 minutos o mayor a 7 dias")
        return
    
    contador = tiempoTrabajo[0]
    tarifaTotal = 0
    
    while  (contador < tiempoTrabajo[1]):
        
        a = dicdias[contador.strftime('%A').upper()]
        #print(a)
        if  (a == 'Lunes' or a == 'Martes' or a == 'Miercoles' or a == 'Jueves' or a == 'Viernes'):
            tarifaTotal = tarifaTotal + tarifa.dias_semana 
        elif (a == 'Sabado' or a == 'Domingo'):
            tarifaTotal = tarifaTotal + tarifa.fines_semana
            
        
        contador = contador + timedelta(hours=1)
        
        
    return tarifaTotal

tarifa = tarifa()
tarifa.dias_semana = float(input('Introduzca la tarifa para los dias de semana (Lun a Vie)'))
tarifa.fines_semana = float(input('Introduzca la tarifa para los fines de semana (Sab y Dom)'))

respuesta = 1
while (0 < respuesta < 3):
    respuesta=int(input(('''Introduzca la opcion que desee 
        1- Modificar montos de las tarifas.
        2- Calcular monto a pagar por un trabajo.
        3- Salir del Sistema.
            ''')))
    
    if respuesta == 1:
        tarifa.dias_semana = float(input('Introduzca la nueva tarifa para los dias de semana (Lun a Vie) \n'))
        tarifa.fines_semana = float(input('Introduzca la nueva tarifa para los fines de semana (Sab y Dom) \n'))

    if respuesta == 2:
        inicioTrabajo = input('Introduzca fecha de inicio del trabajo (dd/mm/aaaa-hh:mm) \n')
        finTrabajo = input('Introduzca fecha de fin del trabajo (dd/mm/aaaa-hh:mm) \n')

        inicioTrabajo = datetime.strptime(inicioTrabajo, formato)
        finTrabajo = datetime.strptime(finTrabajo, formato)

        tiempoTrabajo = [inicioTrabajo,finTrabajo]


        
        print(tiempoTrabajo[1]-tiempoTrabajo[0])
        print("Monto a pagar por el trabajo:", calcularPrecio(tarifa, tiempoTrabajo))    
        print("")
    