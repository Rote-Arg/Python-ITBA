def ahorcado():
    palabra = input("Ingrese la palabra a adivinar ")
    oportunidades = int(input("Ingrese la cantidad de oportunidades "))
    palabra_u = palabra.upper()
    intentos = 0
    contador = 0 
    while oportunidades > intentos:
        letra = input("Ingrese una letra ")
        letra_u = letra.upper()
        if letra_u in palabra_u:
            palabra_u = palabra_u.replace(letra_u, "")
            contador += 1
            if len(palabra_u) == 0:
                print(f"Lo conseguiste en {contador} intentos")
                ahorcado()
        else:
            contador += 1
            intentos += 1
            print(f"te quedan {oportunidades - intentos} intentos")
        if oportunidades == intentos:
            print(f"No lo has conseguido")
            ahorcado()
ahorcado()