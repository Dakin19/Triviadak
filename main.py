import random
import time

puntaje = 0
iniciar_trivia = True
intentos = 0

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'


while iniciar_trivia == True: 
  intentos += 1
  puntaje = random.randint(0, 10)

  print(BLACK+"\nIntento número:", intentos)
  input(BLACK+"Presiona Enter para continuar")

  nombre=input(YELLOW+ "Bienvenido a la trivia de cultura general \n\nEscribe tu Nombre:")
  
  
  print(YELLOW+"\nhola",nombre, "Midamos que tanto sabes de  cultura.")
  time.sleep (1)
  print(GREEN+"Empezarás con ",puntaje, "puntos, a medida que avances, sumarás o restaras puntos.")
  time.sleep (2)
  ppregun1 = input(BLUE+"\nPrimera pregunta:\n\n¿Quién se tiró del morro de Arica?\nA)José pardo\nB)Miguel Grau\nC)Francisco Bolognesi\nD)Alfonso Ugarte\n\nResponde: ")
  
  while ppregun1 not in ("a", "b", "c", "d", "x"):
    print("\nRespuesta no válida, solo escribe la letra de la respuesta correcta.")
    ppregun1 = input("Responde Correctamente: ")
  
  if ppregun1 == "a":
    puntaje -=10
    print("\nJose pardo era un niño!. -10 puntos")
  elif ppregun1 == "b":
    puntaje -=10
    print("\n¿El caballero de los mares? -10 puntos")
  elif ppregun1 == "x":
    puntaje +=10000
    print("\nPillín, encontraste la respuesta secreta :*, toma ", puntaje, " puntos")
  elif ppregun1 == "c":
    puntaje -=10
    print("\nError!!!  -10 puntos")
  else:
    puntaje += random.randint(0, 10)
    print("\nBien", nombre,  "Respuesta correcta")
  
  time.sleep (1)
  print("\nLlevas ", puntaje, " Puntos")
  time.sleep (2)
  ppregun2 = input(MAGENTA+"\nSegunda pregunta:\n\n¿Quién es llamado el brujo de los Andes?\nA)Rosa merino\nB)Héctor Lavoe\nC)El chato grados\nD)Andres Avelino Cáceres\n\nResponde: ")
  
  while ppregun2 not in ("a", "b", "c", "d", "x"):
    print("\nRespuesta no válida, solo escribe la letra de la respuesta correcta.")
    ppregun2 = input("Responde Correctamente: ")
  
  if ppregun2 == "a":
    puntaje -=10
    print("\nRosa fue cantante!. -10 puntos")
  elif ppregun2 == "b":
    puntaje -=10
    print("\nError!, la calle es una selva de cemento, -10 puntos")
  elif ppregun2 == "x":
    puntaje +=10000
    print("\nPillín, encontraste la respuesta secreta :*, toma ", puntaje, " puntos")
  elif ppregun2 == "c":
    puntaje -=10
    print("\nError!, Que linda flor, -10 puntos")
  else:
    puntaje += random.randint(10, 20)
  
    print("\nBien", nombre,  "Respuesta correcta")
    time.sleep (1)
  print("\nLlevas ", puntaje, " Puntos")
  time.sleep (2)
  ppregun3 = input(CYAN+"\nTercera pregunta:\n¿Qué se celebra el 7 de junio?\nA)Mi cumpleaños\nB)Día de los proceres y precursores\nC)Día de la bandera\nD)El cumpleaños de pedro castillo\nResponde: ")
  
  while ppregun3 not in ("a", "b", "c", "d", "x"):
    print("\nRespuesta no válida, solo escribe la letra de la respuesta correcta.")
    ppregun3 = input("Responde Correctamente: ")
    
  if ppregun3 == "a":
    puntaje -=10
    print("\nError, ese día es mi cumpleaños. -10 puntos")
  elif ppregun3 == "b":
    puntaje -=10
    print("\nNo. -10 puntos")
  elif ppregun3 == "x":
    puntaje +=10000
    print("\nPillín, encontraste la respuesta secreta :*, toma ", puntaje, " puntos")
  elif ppregun3 == "d":
    puntaje -=10
    print("\n¿Es enserio? -10 puntos")
  else:
    puntaje += random.randint(20, 50)
    print("\nBien", nombre,  "Respuesta correcta")
    time.sleep (1)
  print("\nLlevas ", puntaje, " Puntos")
  
  print("\n\nPor último, haremos esta pregunta de vida o muerte, si respondes bien, tu puntaje se duplicará, si eliges la mas cercana a la respuesta correcta, tu puntaje aumentará 5 puntos, si eliges la mas cercana a la incorrecta disminuirá en 5 puntos, en cambio si eliges la mas errada, se dividirá tu puntaje a la mitad!, buena suerte! ")
  time.sleep (3)
  ppregun4 = input(RED+"\nÚltima pregunta:\n¿En que año fue la primera asamblea constituyente en el Perú?\nA)1822\nB)1824\nC)1826\nD)1823\nResponde: ")  
  
  while ppregun4 not in ("a", "b", "c", "d", "x"):
    print(+"\nRespuesta no válida, solo escribe la letra de la respuesta correcta.")
    ppregun3 = input("Responde Correctamente: ")
    
  if ppregun4 == "d":
    puntaje +=5
    print("\nBien!, elegiste la mas cercana a la correcta, + 5 puntos.")
  elif ppregun4 == "c":
    time.sleep (1)
    puntaje /=2
    print("\nError!, es la respuesta errone, tu puntaje se dividira a la mitad.")
  elif ppregun4 == "x":
    time.sleep (1)
    print("\nNO HAY RESPUESTA SECRETA.")
  elif ppregun4 == "b":
    time.sleep (1)
    puntaje -=5
    print("\nTu respuesta fue la mas alejada a la certera, -5 puntos.")
  else:
    time.sleep (1)
    puntaje *=2 
    print("\nBien", nombre,  "Duplicaste tu puntaje!")
  time.sleep (2)
  print(WHITE+"\nMuchas gracias por jugar, alcanzaste ", puntaje, " Puntos!")  
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si":  
   print(GREEN+"\nEspero",nombre , " que lo hayas pasadobien, hasta pronto!") 
   iniciar_trivia = False  