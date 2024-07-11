#Exercicio = https://www.hackerrank.com/challenges/apple-and-orange/

# s =  posição inicial da casa
# t = posição final da casa
# a = posição da arvore de maçã
# b = posição da arvore de laranja
# m = quantidade de maçãs
# n = quantidade de laranjas
# apples = vetor com distancias das respectivas maças e da arvore
# oranges = vetor com distancias das respectivas laranjas e da arvore 

s = 7
t = 11
a = 5
b = 15
m = 3
n = 2
posApples = [-2, 2, 1]
posOranges = [5, -6]


def countApplesAndOranges(s, t, a, b, apples, oranges):
    posMaca = 0
    posOrange = 0
    countMacas = 0
    countOranges = 0
    for value in apples:
        posMaca = a + value
        if posMaca >= s and posMaca <= t:
            countMacas += 1
    
    for value in oranges:
        posOrange = b + value
        if posOrange >= s and posOrange <= t:
            countOranges += 1

    print(f'{countMacas}\n{countOranges}')


if __name__ == '__main__':
    countApplesAndOranges(s,t,a,b, posApples, posOranges)
