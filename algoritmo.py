import random 

palabras = ["python", "java", "javascript", "ruby", "php", "html", "css", "csharp", "typescript", "swift"]

def elegir_palabra(lista_palabras):
    return random.choice(lista_palabras)

def juego_ahorcado():
    palabra = elegir_palabra(palabras)
    letras_adivinadas = set()
    intentos_fallidos = 0
    max_intentos = 6

def mostrar_progreso(palabra, letras_adivinas):
    progreso = (letra if letra in letras_adivinas else "_" for letra in palabra)
    return "".join(progreso)

    print("¡Bienvenido al juego juego del Ahorcado!")
    print(f"Tienes {max_intentos} intentos para adivinar la palabra.")


    while intentos_fallidos < max_intentos:
        print(mostrar_progreso(palabra, letras_adivinas))
        letra = input("Adivina una letra:").lower()

        letras_adivinas.add(letra)
        intentos_fallidos += 1
        print(f"Letra incorrecta. Te quedan {max_intentos - intentos_fallidos} intentos.")

    if intentos_fallidos == max_intentos:
        print(F"Lo siento, has perdido. La palabra era: {palabra}")

