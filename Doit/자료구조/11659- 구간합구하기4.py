# 구간 합 구하기 4
# s[n] = s[n-1] + a[n]
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.insert(0,0)

# 구간 합 만들기
S = [0] * (N+1)
for i in range(1, N+1):
    S[i] = S[i-1] + A[i]

for i in range(M):
    start, end = map(int, input().split())
    print(S[end] - S[start-1])