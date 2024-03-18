import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
ary = [[0] * (N+1)]
for _ in range(N):
  tmp =[0] + list(map(int, input().split()))
  ary.append(tmp)

# 누적합 배열 만들기
D = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
  for j in range(1, N+1):
    D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + ary[i][j]

for _ in range(M):
  x1, y1, x2, y2 = map(int, input().split())
  result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
  print(result)

  