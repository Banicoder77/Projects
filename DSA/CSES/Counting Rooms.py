h,w=map(int,input().split())
l=[]
for _ in range(h):
    l.append(list(input()))
roomcount=0
possible=[(0,1),(1,0),(-1,0),(0,-1)]
visited = [[0]*w for _ in range(h)]
def dfs(start):
    index=[start]
    while index:
        curr=index.pop()
        if not visited[curr[0]][curr[1]]:
            visited[curr[0]][curr[1]]=1
            for dx,dy in possible:
                xn=curr[0]+dx
                yn=curr[1]+dy
                if 0<=xn<h and 0<=yn<w and not visited[xn][yn] and l[xn][yn]=='.':
                    index.append((xn,yn))
for i in range(h):
    for j in range(w):
        if l[i][j]=='.' and not visited[i][j]:
            dfs((i,j))
            roomcount+=1
    
print(roomcount)