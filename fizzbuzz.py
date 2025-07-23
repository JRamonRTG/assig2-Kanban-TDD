def fizzbuzz(n):
    for n in range(0, n):
        if n % 3 == 0 and n % 5 == 0:
            print("FizzBuzz - multiplo de ambos")
            print(n)

fizzbuzz(100)