'''

< 요세푸스 문제 >
https://www.acmicpc.net/problem/1158

'''

n, k = map(int, input().split())
q = [i for i in range(1,n+1)]
result = []
idx = 0

while q:
    idx = (idx + (k-1)) % len(q)
    result.append(q.pop(idx))

print('<' + ', '.join(map(str,result)) + '>')