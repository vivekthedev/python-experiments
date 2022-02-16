num = int(input("NUMBER : "))
print(any([x for x in range(2, num // 2) if num % x == 0]))
