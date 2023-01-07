from itertools import combinations, permutations
lst=[1,5,7]
tmp=list(combinations(lst,2))


num=1.35425
print(f'{num:.2f}')

# subset
ary= [10,20,30,40]
n=len(ary)
for num in range(1<<n):         # (1,1<<n) 이면 공집합 제외
    result=[]
    for j in range(n):
        if num&(1<<j):
            result.append(ary[j])

    print(result)