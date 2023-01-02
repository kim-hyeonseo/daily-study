iter=1
while 1:
    a,b,c = map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    else :
        n=c//b
        v=a*n
        n=c%b
        
        if a<n:
            v+=a
        else: v+=n


        print(f'Case {iter}: {v}')
        iter+=1