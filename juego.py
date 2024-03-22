import random
# Lista de palabras posibles

words = ["python", "programacion", "computadora", "codigo", "desarrollo",
"inteligencia"]
vocals = ["a", "e", "i", "o", "u"]

# Elegir una palabra al azar

secret_word = random.choice(words)

# variable de fallos 

failures = 0
max_failures = 10

# Lista para almacenar las letras adivinadas

guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")


print(""" seleccione que modo desea jugar : 
      1- facil : En la palabra se muestran todas las vocales. 
      2- medio : Se muestra la primer y ultima letra de la palabra.
      3-dificil : No se muestra ninguna letra de la palabra. """)
modo = int(input())

# dependiendo del modo agrega las letras en caso de ser necesario a las adivinadas para ser mostradas
if (modo == 1 ):
    for c in secret_word:
        if c in vocals:
            guessed_letters.append(c)
elif (modo == 2 ):
    guessed_letters.append(secret_word[0])
    guessed_letters.append(secret_word[-1])
elif (modo == 3):
    None
else:
    modo = int(input(" ingresa un numero valido para poder jugar"))

# formo la palabra para poder mostrarla (dependiendo del modo ) y empezar a jugar 
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
word_displayed= ""
if modo == 1 or modo == 2 :
    for c in secret_word:
        if c in guessed_letters:
            word_displayed += c
        else:
            word_displayed += "_" 
else:
    word_displayed = "_" * len(secret_word)

# Mostrar la palabra en pantalla 
print(f"Palabra: {word_displayed}")


while failures< max_failures:
     # Pedir al jugador que ingrese una letra
     letter = input("Ingresa una letra: ").lower()
     
     
     # si no ingreso un caracter o ingreso un espacio vacio, se vuelve a pedir hasta q ingrese uno valido
     # no se le descuenta un intento ya que puede ser un error 
     if letter == "" or letter == " ":
         print("error no se ingreso una letra , intentelo de nuevo")
         while letter == "" or letter == " ":
             letter = input("Ingresa una letra valida: ").lower()
     
     # Verificar si la letra ya ha sido adivinada , no cuenta como un fallo si vuelve a ingresarla
     if letter in guessed_letters:
         print("Ya has intentado con esa letra. Intenta con otra.")
         continue
     # Agregar la letra a la lista de letras adivinadas
     guessed_letters.append(letter)
     # Verificar si la letra está en la palabra secreta
     if letter in secret_word:
         print("¡Bien hecho! La letra está en la palabra.")
     else:
         print("Lo siento, la letra no está en la palabra.")
         failures += 1
     # Mostrar la palabra parcialmente adivinada
     letters = []
     for letter in secret_word:
         if letter in guessed_letters:
             letters.append(letter)
         else:
             letters.append("_")
     word_displayed = "".join(letters)
     print(f"Palabra: {word_displayed}")
     # Verificar si se ha adivinado la palabra completa
     if word_displayed == secret_word:
         print(f"¡Felicidades! Has adivinado la palabra secreta: {secret_word}")
         break
else:
     print(f"¡Oh no! Has agotado tus {failures} fallos.")
     print(f"La palabra secreta era: {secret_word}")