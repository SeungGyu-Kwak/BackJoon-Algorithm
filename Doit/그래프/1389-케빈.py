# 케빈 베이컨의 6단계 법칙
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
            

distance = [[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]

for i in range(1,N+1):
  distance[i][i] = 0

for _ in range(M):
  a, b = map(int, input().split())
  distance[a][b] = 1
  distance[b][a] = 1

# 플로이드 워셜 수행
for k in range(1, N+1):
  for i in range(1, N+1):
    for j in range(1, N+1):
      if distance[i][j] > distance[i][k] + distance[k][j]:
        distance[i][j] = distance[i][k] + distance[k][j]

Min = sys.maxsize
Answer = -1

for i in range(1, N+1):
  temp = 0
  for j in range(1, N+1):
    temp += distance[i][j] 
  if Min > temp:
    Min = temp
    Answer = i
print(Answer)