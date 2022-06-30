from math import sqrt
def square(a):
    l = []
    per = 4*a
    l.append(per)
    pl = a*a
    l.append(pl)
    diag = a*sqrt(2)
    l.append(diag)
    t = tuple(l)
    return t

print(square(int(input('Enter: '))))