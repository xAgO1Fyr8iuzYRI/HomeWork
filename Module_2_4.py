numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i <= 1:
        continue
    else:
        deliteli = 0
        for j in range(2, i + 1):
            if i % j == 0:
                deliteli = deliteli + 1
            else:
                continue
    if deliteli > 1:
        not_primes.append(i)
    else:
        primes.append(i)
print('Primes:',primes)
print('Not Primes:',not_primes)
