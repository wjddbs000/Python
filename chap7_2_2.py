import sympy

print(sympy.isprime(5))
count = 0
lists = []
for i in range(100,1000):
    if sympy.isprime(i) is True:
        count += 1
        lists.append(i)

print("100부터 1000까지의 소수 갯수{}",count)
print("소수 리스트",lists)

print(list(sympy.primerange(1,100)))