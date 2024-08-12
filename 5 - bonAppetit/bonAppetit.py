bill = [3,10,2,9]
k = 1
b = 12



def bonAppetit(bill, k, b):
    total = sum(bill)

    anna = (total - bill[k])/2
    
    if b == anna:
        print('Bon Appetit')
    else:
        print(int(b - anna))



if __name__ == '__main__':
    bonAppetit(bill, k, b)