# 단지번호 붙이기
# dfs로 풀어보자
import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt', 'r')

N = int(input()) # N x N 받기
ary = []
for _ in range(N): # N x N 생성
  tmp = list(map(int, input()))
  ary.append(tmp)

count = 0 # 총 단지 수 받을 변수
countAry = [] # 각 단지내 집의 수 담을 리스트
home = 0

def dfs(x, y):
  dx = [-1, 0, 1, 0] # 북 동 남 서 순서
  dy = [0, 1, 0, -1]
  global home
  # 범위 체크
  if x <= -1 or x >= N or y <= -1 or y >= N:
    return False
  if ary[x][y] == 1: # 집이 있으면
    ary[x][y] = 0 # 방문처리
    home += 1
    for i in range(4):
      dfs(x + dx[i], y + dy[i])
    return True
  return False

for i in range(N):
  for j in range(N):
    if dfs(i,j) == True:
      count += 1
      countAry.append(home)
      home = 0

print(count)
countAry.sort()
for c in countAry:
  print(c)