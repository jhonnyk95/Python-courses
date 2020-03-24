def rectangulo(ancho, alto):
    for i in range(alto):
        for j in range(ancho):
            print("* ", end="")
        print()
rectangulo(4, 2)