n = int(input())

fact = 1
for i in range(1, n+1):
    fact *= i

num_digits = len(str(fact))
print(num_digits)



