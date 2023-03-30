# 다리 만들기 2
import sys
import copy
from queue import PriorityQueue
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

N, M = map(int, input().split())
myMap = [[0 for j in range(M)] for i in range(N)]
visited = [[False for j in range(M)] for i in range(N)]

# 데이터 저장
for i in range(N):
  myMap[i] = list(map(int, input().split()))

sNum = 1 # 섬 번호
sumList = list([]) # 모든 섬 정보 이중리스트
mlist = [] # 1개의 섬 정보 리스트

def addNode(i, j, queue):
  myMap[i][j] = sNum
  visited[i][j] = True
  temp = [i,j]
  mlist.append(temp)
  queue.append(temp)

def BFS(i,j):
  queue = deque()
  mlist.clear()
  start = [i,j]
  queue.append(start)
  mlist.append(start)
  visited[i][j] = True
  myMap[i][j] = sNum
  while queue:
    r,c = queue.popleft()
    for d in range(4):
      tempR = dx[d]
      tempC = dy[d]
      while r + tempR >= 0 and r + tempR < N and c + tempC >= 0 and c + tempC < M:
        if not visited[r+tempR][c+tempC] and myMap[r+ tempR][c+tempC] != 0:
          addNode(r+tempR, c+tempC, queue)
        else:
          break
        if tempR < 0:
          tempR -= 1
        elif tempR >0:
          tempR += 1
        if tempC < 0:
          tempC -= 1
        elif tempC >0:
          tempC += 1
  return mlist

for i in range(N):
  for j in range(M):
    if myMap[i][j] != 0 and not visited[i][j]:
      tempList = copy.deepcopy(BFS(i,j))
      sNum += 1
      sumList.append(tempList)

pq = PriorityQueue()

for now in sumList:
  for temp in now:
    r = temp[0]
    c = temp[1]
    now_S = myMap[r][c]
    for d in range(4): # 4방향 검색
      tempR = dx[d]
      tempC = dy[d]
      blength = 0
      while r + tempR >= 0 and r + tempR < N and c + tempC >= 0 and c + tempC < M:
        if myMap[r + tempR][c + tempC] == now_S:
          break
        elif myMap[r + tempR][c + tempC] != 0:
          if blength > 1:
            pq.put((blength, now_S, myMap[r+tempR][c + tempC]))
            break
          else:
            blength += 1
          if tempR < 0:
            tempR -= 1
          elif tempR >0:
            tempR += 1
          if tempC < 0:
            tempC -= 1
          elif tempC >0:
            tempC += 1
def find(a):
  if a == parent[a]:
    return a
  else:
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
  a = find(a)
  b = find(b)
  if a != b:
    parent[b] = a

parent = [0] * sNum

for i in range(len(parent)):
  parent[i] = i

useEdge = 0
result = 0

while pq.qsize()>0:
  v, s, e = pq.get()
  if find(s) != find(e):
    union(s,e)
    result += v
    useEdge += 1

if useEdge == sNum - 2:
  print(result)
else:
  print(-1)