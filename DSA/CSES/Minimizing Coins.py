from array import array
n, x = map(int, input().split())
c = list(map(int, input().split()))
 
INF = int(1e9)
dp = array('i', [INF] * (x + 1))
dp[0] = 0
 
for coin in c:
    for i in range(coin, x + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)
 
print(dp[x] if dp[x] != INF else -1)