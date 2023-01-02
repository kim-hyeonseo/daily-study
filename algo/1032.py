iter=int(input())
ary=[list(input()) for _ in range(iter)]

size=len(ary[0])
lst=['-']*size


for j in range(size):
    flag=1
    for i in range(1,iter):
        if ary[0][j]==ary[i][j]:
            pass
        else : flag=0

    if flag:
        lst[j]=ary[0][j]
    else : lst[j]='?'

print(''.join(lst))



        

        