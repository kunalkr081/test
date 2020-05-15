input= int(input())

x = 1

while (input != 0):

    if x % 5 != 0:

        print(x, end=' ')

        input-=1

        x+=2

    else:
 
        x+=2