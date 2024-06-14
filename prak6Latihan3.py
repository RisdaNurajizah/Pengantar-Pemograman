bilangan = 11

# Menghitung nilai Fibonacci
def fibonacci(n):
    fib_sequence = [1, 1]
    while len(fib_sequence) < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence[:n]

result = fibonacci(bilangan)

# mencetak hasil secara vertikal
for angka in result:
    print(angka)
