# 구간 합 구하기 5
# DP 알고리즘을 사용하기
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
ary = [[0]*(N+1)]
dAry = [[0]*(N+1) for _ in range(N+1)]

# ary 받기 1부터 시작하기 위해 1,1부터 값 넣기
for i in range(N):
  ary_row = [0] + [int(x) for x in input().split()]
  ary.append(ary_row)

# 합배열 만들기
for i in range(1, N+1):
  for j in range(1, N+1):
    dAry[i][j] = dAry[i-1][j] + dAry[i][j-1] - dAry[i-1][j-1] + ary[i][j]

# 결과 출력하기
# ex) 2 2 3 4 이면 d[x2][y2] - d[x1-1][y2] - d[x2][y1-1] + d[x1-1][y1-1]

for i in range(M):
  x1, y1, x2, y2 = map(int, input().split())
  result = dAry[x2][y2] - dAry[x1-1][y2] - dAry[x2][y1-1] + dAry[x1-1][y1-1]
  print(result)


