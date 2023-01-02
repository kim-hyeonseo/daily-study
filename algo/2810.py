L=int(input())
s=input()
lst=['*']*(2*L+1)

i=1
j=0
while j<L:
    if s[j]=='S':
        lst[i]='S'
        i+=2
        j+=1
    elif s[j]=='L':
        lst[i]='L'
        lst[i+1]='L'
        j+=2
        i+=3
while 1:
    if len(lst)==0: break
    elif lst[-1]=='*':
        lst.pop()
    else: break


print(min(len(lst)+1-L,L))
