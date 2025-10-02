# pedir edad
edad_mago = input("Introduce la edad del mago: ")
# convertir a entero
try:
  edad_mago = int(edad_mago)
except: 
  # si falla, pon 100
  edad_mago = 100

# clasifica por edad
# menor que 30 es Aprendiz
if edad_mago < 30: 
  classificacion_mago = "Aprendiz"
  print("EL mago es: ",classificacion_mago)
# de 30 a 99 es Hechicero
elif edad_mago >= 30 and edad_mago <= 99:
  classificacion_mago = "Hechicero"
  print("EL mago es: ",classificacion_mago)
# mas de 100 es Archimago
elif edad_mago >= 100:
  classificacion_mago = "Archimago"
  print("EL mago es: ",classificacion_mago)

# funcion poderBase, recibe edad, devuelve entero
def poderBase(edad):
  # si es aprendiz, devuelve 5
  if classificacion_mago == "Aprendiz":
    return 5
  # si es hechicero, devuelve 8
  elif classificacion_mago ==  "Hechicero":
    return 8
  # si es archimago, devuelve 10
  elif classificacion_mago ==  "Archimago":
    return 10
poder = poderBase(edad_mago)

# escudo empieza con 15 puntos
escudo = 15

# empezamos bucle
for turno in range(1,3):

# recorre dos turnos con for
 if turno == 1:
   # turno 1 fuego daño = poderBase // 2
   print("Turno 1 --> Hechizo de Fuego")
   daño = poder//2
   assert isinstance(daño, int) and daño >= 0, "El daño debe ser numérico y >= 0"
   assert escudo >= 0, "El escudo no puede ser negativo"

 else:
   # turno 2 hechizo rayo = daño = poderBase // 3
   print("Turno 2 --> Hechizo de Rayo")
   daño = poder//3
 assert isinstance(daño, int) and daño >= 0, "El daño debe ser numérico y >= 0"
 assert escudo >= 0, "El escudo no puede ser negativo"

   
 # resta el daño al escudo
 escudo = escudo - daño
 print("El escudo a recibido: ",daño,"daño y le queda",escudo,"de protección" )
 # si energia escudo baja de cero, ajusta a cero
 if escudo < 0:
   escudo = 0
 else: 
   print("Energia escudo mayor a 0")

print("Datos del mago, edad: ",edad_mago,"Rango: ",classificacion_mago,"Poder base: ",poder,"Energia del escudo:  ",escudo)

if escudo == 0:
  print("Mago rompe escudo")
  print("🏆WINER!🏆")
else:
  print("El escudo resite el duelo")
  print("🌩️ GAME OVER 🌩️")
  
# tras cada daño, print de daño y mayor que cero
# tras ajuste energia, print y energia es mayor que cero

# salida: edad, rango, poder base, energia del escudo
# energia es cero, mago rompe escudo
# energia mayor que cero, escudo resiste duelo
