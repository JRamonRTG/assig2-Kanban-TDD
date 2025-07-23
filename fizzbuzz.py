# fizzbuzz.py
# Imprime Fizz, Buzz o FizzBuzz segun los multiplos encontrados entre 0 y n
# este ira de un rango de 0 a n


def fizzbuzz(n):
    for n in range(0, n):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz - multiplo de ambos")
            print(n)
        elif n % 3 == 0:
            print("Fizz - multiplo de 3")
            print(n)
            print("-----------------------------")
        elif n % 5 == 0:
            print("Buzz - multiplo de 5")
            print(n)
            print("-----------------------------") 

#de ser requerido, puede cambiarse el rango en la linea 22 de la funciona fizzbuzz(n)

fizzbuzz(100)