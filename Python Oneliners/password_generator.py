from string import printable as p, whitespace as w
from random import sample as s

print(''.join(s(list(set(p) - set(w)), k=int(input("ENTER LENGTH : ")))))
