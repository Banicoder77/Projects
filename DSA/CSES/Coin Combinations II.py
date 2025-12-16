_,x=map(int,input().split())
coinlist=list(map(int,input().split()))
MOD=10**9+7
dp=[0]*7**8
dp[0]=1
for coin in coinlist:
    for i in range(x+1-coin):
            dp[i+coin]+=dp[i]
            dp[i+coin]%=MOD
print(dp[x])