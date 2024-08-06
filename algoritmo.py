import random

palabras = ["python", "java", "javascript", "ruby", "php", "html", "css", "csharp", "typescript", "swift"]

def elegir_palabra(lista_palabras):
    return random.choice(lista_palabras)

def juego_ahorcado():
    palabra = elegir_palabra(palabras)
    letras_adivinadas = set()
    intentos_fallidos = 0
    max_intentos = 6


