# 플로이드

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input()) # 도시의 개수
M = int(input()) # 버스의 개수

D = [[sys.maxsize for _ in range(N+1)] for _ in range(N+1)] # 인접행렬 만들기
# 인접행렬 초기화
for i in range(1,N+1):
  D[i][i] = 0

# 인접행렬에 값 저장
for _ in range(M):
  s, e, w = map(int, input().split())
  if D[s][e] > w:
    D[s][e] = w

# 플로이드-워셜 알고리즘 수행
for k in range(1, N+1):
  for i in range(1, N+1):
    for j in range(1, N+1):
      if D[i][j] > D[i][k] + D[k][j]:
        D[i][j] =  D[i][k] + D[k][j]

# 정답 출력
for i in range(1, N+1):
  for j in range(1, N+1):
    if D[i][j] == sys.maxsize:
      print(0, end = ' ')
    else:
      print(D[i][j], end = ' ')
  print()