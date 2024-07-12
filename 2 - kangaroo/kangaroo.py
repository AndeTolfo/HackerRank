# Exercício -> https://www.hackerrank.com/challenges/kangaroo/


# x1 = PosIni canguru 1 
# v1 = Velocidade canguru 1
# x2 = PosIni canguru 2 
# v2 = Velocidade canguru 2


x1 = 0
v1 = 3
x2 = 4
v2 = 2

def kangaroo(x1,v1,x2,v2):
    if (x1 > x2 and v1 >= v2) or (x2 > x1 and v2 >= v1):
        return 'NO'
    
    if (x1 - x2) % (v1 - v2) == 0:
        return 'YES'

    return 'NO'


if __name__ == '__main__':
    print(kangaroo(x1,v1,x2,v2))