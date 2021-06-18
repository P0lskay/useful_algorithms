n = int(input())
digits = []
chek = False
i = 1
p = 0
while p != n:
    if p > n:
        p -= digits[-1] + digits[-2]
        digits = digits[0:-2]
        p+=n-sum(digits)
        digits.append(n-sum(digits))
    else:
        p += i
        digits.append(i)
        i += 1
print(len(digits))
print(*digits)