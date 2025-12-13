x=input()
mx=0
i=1
prev=x[0]
c=1
while i<len(x):
    if x[i]==prev:
        c+=1
    else:
        mx=max(mx,c)
        c=1
    prev=x[i]
    i+=1
print(max(mx,c))