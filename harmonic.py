def harmonic(n):
    total = 0.0
    for i in range(1, n + 1):
        total += 1.0 / i
    return total

print(harmonic(1))
print(harmonic(2))
print(harmonic(3))
print(harmonic(10))