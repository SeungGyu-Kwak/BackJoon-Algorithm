# 구간 합 구하기 4
# s[n] = s[n-1] + a[n]
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


N, M = map(int, input().split()) # 수 개수, 합을 구해야 하는 횟수
A = list(map(int, input().split())) # 수 리스트
S = [0] * (N+1) # 구간 합 구할 리스트
A.insert(0, 0)
# 구간 합 구하기
S[0] = 0
for i in range(1, N+1):
  S[i] = S[i-1] + A[i]

for i in range(M):
  a, b = map(int, input().split())
  print(S[b] - S[a-1])