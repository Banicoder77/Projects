n=int(input())
l=list(map(int,input().split()))
m=l[0]
c=0
for i in l:
    if i<m:
        c+=m-i
    else:
        m=i
print(c)