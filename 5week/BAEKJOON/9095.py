'''

< 1,2,3 더하기 >
https://www.acmicpc.net/problem/9095

'''

dp = [0,1,2,4]
t = int(input())

for i in range(4, 11):
    dp.append(dp[i-3] + dp[i-2] + dp[i-1])

for _ in range(t):
    print(dp[int(input())])



'''

1 : (1)
2 : (1,1), (2)
3 : (1,1,1), (1, 2), (2,1), (3)
4 : (1,1,1,1), (1,1,2), (1,2,1), (1,3), (2, 1, 1) , (2, 2), (3, 1) 


'''