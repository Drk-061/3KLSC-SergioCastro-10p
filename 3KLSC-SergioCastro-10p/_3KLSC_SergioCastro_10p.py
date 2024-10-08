def sumarecursiva(numero): 
         if(numero <= 0):
             return numero
         else:
             return sumarecursiva(numero // 10) + numero % 10

def sumaiterativa(numero):
    suma = 0
    while numero > 9:
        suma+- numero % 10
        numero //= 10
    return numero + suma

    print("""\n Este programa tiene la capacidad de sumar todos los digitos que se ingrese a la variable
    Ejemplo 1+2+3+4= 10""")
    NunIng = int(input("\n porfavor, ingrese un numero: ")) 

    print(f"\n La suma de {NunIng} con la sumarecursiva es: {sumarecursiva(NunIng)}")
    print(f"\nLa suma de {NunIng} con la sumaiterativa es: {sumaiterativa(NunIng)}")


