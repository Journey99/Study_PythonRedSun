'''

< 1로 만들기 >
https://www.acmicpc.net/problem/1463
- 다이나믹 프로그래밍 이용 : 큰 문제를 작은 문제들로 분할하여 푸는 법

'''

n = int(input())
dp = [0,0,1,1]

if n >= 4:
    for i in range(4, n+1):
        dp.append(dp[i-1] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i//2] + 1, dp[i])
        if i % 3 == 0:
            dp[i] = min(dp[i//3] + 1, dp[i])

print(dp[n])