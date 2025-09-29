
nombre_dragon_a = input("Dime el nombre del dragón A: ")
edad_dragon_a = input("Dime la edad del dragón A: ")
clasificacion_dragon_a = ""
fuerza_dragon_a = 0
resistencia_dragon_a = 0
vida_dragon_a = 50

print("El nombre del dragon A es:",nombre_dragon_a)
print("La edad del dragon A es:",edad_dragon_a)

nombre_dragon_b = input("Dime el nombre del dragón B: ")
edad_dragon_b = input("Dime la edad del dragón B: ")
clasificacion_dragon_b = ""
fuerza_dragon_b = 0
resistencia_dragon_b = 0
vida_dragon_b = 50

print("El nombre del dragon B es:",nombre_dragon_b)
print("La edad del dragon B es:",edad_dragon_b)

# En este bloque me aseguro de que son enteros #######################

try:
  edad_dragon_a = int(edad_dragon_a)
  print("He convertido la edad A correctamente")
except:
  edad_dragon_a = 100
  print("No he convertido la edad A correctamente, asigno 100")
  
try:
  edad_dragon_b = int(edad_dragon_b)
  print("He convertido la edad B correctamente")
except:
  edad_dragon_b = 100
  print("No he convertido la edad B correctamente, asigno 100")

# En este bloque clasifico a los dragones #######################

if edad_dragon_a < 50:
  clasificacion_dragon_a = "Joven"
elif edad_dragon_a >= 50 and edad_dragon_a <= 199:
  clasificacion_dragon_a = "Adulto"
elif edad_dragon_a >= 200:
  clasificacion_dragon_a = "Anciano"
print("El dragon A es:",clasificacion_dragon_a)
  
if edad_dragon_b < 50:
  clasificacion_dragon_b = "Joven"
elif edad_dragon_b >= 50 and edad_dragon_b <= 199:
  clasificacion_dragon_b = "Adulto"
elif edad_dragon_b >= 200:
  clasificacion_dragon_b = "Anciano"
print("El dragon B es:",clasificacion_dragon_b)

# Ahora los vamos a entrenar ###################################

for dia in range (1,4):
  # Como entrenar a tu dragon A
  if clasificacion_dragon_a == "Joven":
    fuerza_dragon_a += 2
    resistencia_dragon_a += 2
  elif clasificacion_dragon_a == "Adulto":
    fuerza_dragon_a += 1
    resistencia_dragon_a += 1
  elif clasificacion_dragon_a == "Anciano":
    fuerza_dragon_a += 1
    resistencia_dragon_a += 1
  print("Final del dia",dia)
  print("El dragon A ahora tiene ",fuerza_dragon_a,"de fuerza y ",resistencia_dragon_a,"de resistencia")
  # Como entrenar a tu dragon B
  if clasificacion_dragon_b == "Joven":
    fuerza_dragon_b += 2
    resistencia_dragon_b += 2
  elif clasificacion_dragon_b == "Adulto":
    fuerza_dragon_b += 1
    resistencia_dragon_b += 1
  elif clasificacion_dragon_b == "Anciano":
    fuerza_dragon_b += 1
    resistencia_dragon_b += 1
  print("Final del dia",dia)
  print("El dragon B ahora tiene ",fuerza_dragon_b,"de fuerza y ",resistencia_dragon_b,"de resistencia")

# DUELO  ##############################################################################
print("Comienza el duelo")
print("Vida dragón A",vida_dragon_a)
print("Vida dragón B",vida_dragon_b)
turno = 1

while vida_dragon_b > 0 and vida_dragon_a > 0:

 print("Turno",turno)

 # Ataque dragón A a dragón B
 for intento in range(2):
  dano_a = (resistencia_dragon_b - fuerza_dragon_a)
  vida_dragon_b -= dano_a
  if vida_dragon_b < 0:
   vida_dragon_b = 0
  print(nombre_dragon_a,"ataca con",dano_a,"Salud",nombre_dragon_b,"queda en: ",vida_dragon_b)
  assert vida_dragon_b >= 0
  if vida_dragon_b == 0:
   break



 # Ataque dragón B a dragón A
 for intento in range(2):
  dano_b = (resistencia_dragon_a - fuerza_dragon_b)
  vida_dragon_a -= dano_b
  if vida_dragon_a < 0:
   vida_dragon_a = 0
  print(nombre_dragon_b,"ataca con",dano_b,"Salud",nombre_dragon_a,"queda en: ",vida_dragon_a)
  assert vida_dragon_a >= 0
  if vida_dragon_a == 0:
   break
 turno += 1
 if turno == 50:
  break

# RESULTADO FINAL ############################################################

print(nombre_dragon_a,"Classificación: ",clasificacion_dragon_a,"Fuerza: ",fuerza_dragon_a,"Vida: ", vida_dragon_a)
print(nombre_dragon_b,"Classificación: ",clasificacion_dragon_b,"Fuerza: ",fuerza_dragon_b,"Vida: ", vida_dragon_b)

if vida_dragon_a > vida_dragon_b: 
 print("El ganador es: ",nombre_dragon_a,"🏆")

elif vida_dragon_b > vida_dragon_a:
 print("El ganador es: ",nombre_dragon_b,"🏆")

else:
  print("Empate!🤝")
