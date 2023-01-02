v=1000-int(input())

money=[500,100,50,10,5,1]
cnt=0
i=0

while v!=0:
    cnt+=v//money[i]
    v%=money[i]
    i+=1

print(cnt)