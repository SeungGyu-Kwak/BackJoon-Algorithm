# 평범한 배낭 0-1 문제

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split()) # 물품의 수, 가방 무게


DP = [[0 for _ in range(K+1)] for _ in range(N+1)]


A = [[0,0]]
# 각 물건의 무게와 가치에 대해 저장
for i in range(N):
    weight, value = map(int, input().split())
    A.append([weight, value])

for i in range(1, N+1):
    for j in range(1, K+1):
        w = A[i][0]
        v = A[i][1]
        
        if j < w: # 현재 weight보다 작으면
            DP[i][j] = DP[i-1][j] # 위의 값을 그대로 가지고 온다.
        else:
            DP[i][j] = max(v + DP[i-1][j-w], DP[i-1][j])

print(DP[N][K])