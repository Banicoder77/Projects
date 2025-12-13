x=int(input())
j=[str(x)]
while x!=1:
    if x%2==0:
        x=x//2
    else:
        x=3*x+1
    j.append(str(x))
print(" ".join(j))