a = int(input())

for i in range(1,a+1):

    if i % 2 == 0 or i%5 == 0:

        for j in range(i, 0, -1):

            print(j,end='*')

    else:
 
       for j in range(1,i+1):

            print(j, end= '*')

    print()