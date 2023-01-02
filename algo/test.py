n,k=map(int,input().split())
lst=list(map(int,input().split()))

for _ in range(k):
    a,b=input().split()
    a-=1
    # tmp=lst[a:b]
    
    result=sum(lst[a-1:b])/(b-a+1)
    print(result)