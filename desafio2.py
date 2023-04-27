def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib = [0, 1]
        while len(fib) < n:
            fib.append(fib[-1] + fib[-2])
        return fib

numero = int(input("Digite um número: "))
sequencia = fibonacci(numero)

if numero in sequencia:
    print(f"O número {numero} pertence à sequência de Fibonacci: {sequencia}")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci: {sequencia}")

