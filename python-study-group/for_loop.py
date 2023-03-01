#break continue
n = 0
while( n <= 12):
    if(n % 2 == 0):
        if n == 10:
            n+=1
            break
        else:
            print(n, "is a even number")
    n+=1

