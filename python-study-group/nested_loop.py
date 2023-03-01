#    1
#   1 2 
#  1 2 3
# 1 2 3 4
n = 11

for i in range(1,n):# 2
    for s in range(1,n-i):
        print(" ",end="")
    for j in range(1,i+1):
       print (j,end=" ")
    print ()

#  for j in range(1,i+1): # range(1,2+1) # 1 2
#     print(j,end=" ")
# print()