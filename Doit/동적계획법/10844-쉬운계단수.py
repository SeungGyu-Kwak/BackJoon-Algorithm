# 쉬운 계단 수
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

S = [0] * 91
S[1] = 1
S[2] = 1

for i in range(3, 91):
    S[i] = S[i-1] + S[i-2]

N = int(input())
print(S[N])

N = int(input())
mod = 1000000000
D = [[0 for _ in range(11)] for _ in range(N+1)]

for i in range(1,10):
  D[1][i] = 1

for i in range(2, N+1):
  D[i][0] = D[i-1][1]
  D[i][9] = D[i-1][8]

  for j in range(1, 9):
    D[i][j] = (D[i-1][j-1] + D[i-1][j+1]) % mod
  
  sum = 0
for i in range(10):
  sum = (sum + D[N][i]) % mod
  
print(sum)