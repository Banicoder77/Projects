h,w=map(int,input().split())
l=[]
for _ in range(h):
    l.append(list(input()))
roomcount=0
index=[(0,0)]
possible=[(0,1),(1,0)]
visited=set()
while index:
    curr=index.pop()
    if curr not in visited:
        visited.add(curr)
        for dx,dy in possible:
            xn=curr[0]+dx
            yn=curr[1]+dy
            if 0<=xn<h and 0<=yn<w and (xn,yn) not in visited:
                index.append((xn,yn))

    print(curr)
    
