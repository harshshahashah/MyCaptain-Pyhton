a = 0
b = 1
n = int(input("How many fibonacci terms you need?(other than 0 and 1) : "))
i = 0
print(a)
print(b)
while i < n:
    sum = a + b
    print(sum)
    a = b
    b = sum
    i = i + 1

