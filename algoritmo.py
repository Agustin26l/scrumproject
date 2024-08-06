if all(letra in letras_adivinadas for letra in palabra):
    print(f"¡Felicidades! Adivinaste la palabra: {palabra}")
    break
else:
    if letra in letras_adivinadas:
        print("Ya has adivinado esa letra. Intenta con otra.")
    elif letra in palabra:
        letras_adivinadas.add(letra)
        
    if__name__=="__main__":
    juego_ahorcado()