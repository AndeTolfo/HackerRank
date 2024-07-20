# Exercício -> https://www.hackerrank.com/challenges/the-birthday-bar/


# s = números
# d = dia do aniversário
# m = mês 


s = [2,2,1,3,2]
d = 4
m = 2

def birthday(s, d, m):
    n = len(s)
    qtd = 0
    soma = 0

    for i in range(n - m + 1):
        soma = sum(s[i:i+m]) 

        if soma == d:
            qtd += 1
    return qtd   
        
            


if __name__ == '__main__':
    print(birthday(s, d, m))
