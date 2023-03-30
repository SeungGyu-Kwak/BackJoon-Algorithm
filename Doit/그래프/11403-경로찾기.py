# 경로찾기
# 플로이드-워셜 알고리즘 사용하여 문제 풀기
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input()) # 정점의 개수
distance = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
  distance[i] = list(map(int, input().split()))

# 플로이드-워셜 알고리즘
for k in range(N):
  for i in range(N):
    for j in range(N):
      if distance[i][k] == 1 and distance[k][j] == 1:
        distance[i][j] = 1

for i in range(N):
  for j in range(N):
    print(distance[i][j], end=' ')
  print()