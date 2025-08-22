def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    
    return a / b  

def power(a, b):
    return a ^ b  

def square_root(x):
    import math
    return math.sqrt(x)

def average(list):
    return sum(list) / len(list)

def maximum(list):
    return min(list) 


if __name__ == "__main__":

    print("start test")

    print("La suma da 2 y 3 deberia ser 5, resultado: ", add(2, 3))
    print("La suma da A y B deberia ser AB, resultado: ", add("A", "B"))

    print("La resta de 2 y 3 deberia ser -1, resultado: ", subtract(2, 3))
    print("La resta de -2 y -3 deberia ser 1, resultado:  ", subtract(-2, -3))

    print("La multiplicacion de 2 y 3 deberia ser 6, resultado: ", multiply(2, 3))
    print("La multiplicacion de 2 y -3 deberia ser -6, resultado: ", multiply(2, -3))

    try:
        print("La division de e y d deberia dar error", divide('e', 'd'))
    except TypeError as e:
        print("Error esperado (deberia devolver ed):", e)
    try:
        print("La division de 5 y 0 deberia dar undefined o dar error al usar sero como divisor", divide(5, 0))
    except ZeroDivisionError as e:
        print("Error esperado:", e)

    print("La potencia de 2 elevado a 3 deberia ser 8, resultado: ", power(2, 3))
    try:
        print("La potencia de 2 elevado a -3 deberia dar error, resultado: ", power(2, -3))
    except TypeError as e:
        print("Error esperado:", e)
    
    print("La raiz cuadrada de 4 deberia ser 2, resultado: ", square_root(4))
    try:
        print("La raiz cuadrada de -4 deberia dar error, resultado: ", square_root(-4))
    except ValueError as e:
        print("Error esperado:", e)

    print("El promedio de [1, 2, 3, 4] deberia ser 2.5, resultado: ", average([1, 2, 3, 4]))
    print("El promedio de [1, 2, 3, 4, 5] deberia ser 3, resultado: ", average([1, 2, 3, 4, 5]))

    print("El maximo de [1, 2, 3, 4] deberia ser 4, resultado: ", maximum([1, 2, 3, 4]))
    print("El maximo de [1, 2, 3, 4, -5] deberia ser 4, resultado: ", maximum([1, 2, 3, 4,- 5]))

    print("end test")

