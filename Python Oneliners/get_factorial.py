fact = lambda x: x * fact(x-1) if  x != 1  else x
print(fact(int(input("ENTER NUMBER : "))))