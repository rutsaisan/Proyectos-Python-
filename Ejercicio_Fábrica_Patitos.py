'''
Escribe un programa en Python que utilice bucles for para simular el conteo de patitos de goma en una fábrica. 

El programa debe recorrer: 

Los años de producción (por ejemplo, de 2000 a 2025). 

Los meses del año (de 1 a 12). 

Los días del mes (del 1 al 30). 

Por cada día, el programa mostrará un mensaje indicando cuántos patitos de goma se han fabricado ese día. 

Requisitos adicionales: 

Cada día se fabrican exactamente 10 patitos de goma. 

El programa debe mostrar mensajes como: 

Día 5 del mes 3 del año 2010: 10 patitos de goma fabricados 

Al terminar el bucle, el programa debe mostrar el total de patitos fabricados en todo el período. 
'''

patos = 10
for anio in range(1978,2025):
 for mes in range(1,12):
  for dia in range(1,31):
   print("Hoy es el dia ",dia,"del mes",mes,"del año",anio,"Se han fabeicado hoy 10 paritos")
   patos += 10

print("En total se han fabricado",patos,"patitos")
