a, b = 0, 1
fibonacci = []

while a <= 500:
    fibonacci.append(a)
    a, b = b, a + b

print("Série de Fibonacci até 500:", fibonacci)