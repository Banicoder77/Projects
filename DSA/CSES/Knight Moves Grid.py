n=int(input())
l=[[float('inf')]*n for _ in range(n)]
l[0][0]=0
moves=[(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-1,2),(-2,1),(-2,-1)]
from collections import deque
q=deque()
q.append((0,0))
while q:
    x,y=q.popleft()
    for dx,dy in moves:
        nx=x+dx
        ny=y+dy
        if 0 <= nx < n and 0 <= ny < n and l[nx][ny] > l[x][y] + 1:
            l[nx][ny] = l[x][y] + 1
            q.append((nx, ny))
 
for row in l:
    print(' '.join(map(str, row)))