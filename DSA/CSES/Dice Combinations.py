from array import array
n=int(input())
MOD=10**9+7
pos=[i for i in range(1,7)]
dp=array('l',[0]*(n+1))
dp[0]=1
for i in range(1,n+1):
    for coin in pos:
        if i-coin>=0:
            dp[i]+=dp[i-coin]%MOD
print(dp[n]%MOD)