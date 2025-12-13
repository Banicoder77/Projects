x=int(input())
j=list(map(int,input().split()))
l=[False]*x
for i in j:
    l[i-1]=True
for c,d in enumerate(l):
    if d==False:
        print(c+1)
        break