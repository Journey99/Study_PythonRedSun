'''

백준 - https://pacific-ocean.tistory.com/194


n 개수
1  1
2  3
3  5
4  11
5  21
...

'''


dp = [0,1,3]
for i in range(3, 1001):
    dp.append(dp[i-2]*2 + dp[i-1])

n = int(input())
print(dp[n] % 10007)