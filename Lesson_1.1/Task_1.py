
n = 123

# Введите ваше решение ниже
i=0
res = 0
for i in range(n):
    res += n % 10
    n = n//10
print(res)