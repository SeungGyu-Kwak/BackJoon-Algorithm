import sys
from queue import PriorityQueue
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input()) # 연산의 개수 입력받기

# 우선순위 큐 설정, put: 삽입, get : 삭제
myQueue = PriorityQueue()

for i in range(N):
  n = int(input())
  if n == 0:
    if myQueue.empty():
      print('0')
    else:
      tmp = myQueue.get()
      print(tmp[1])
  else:
    myQueue.put((abs(n), n)) # 절댓값을 기준으로 정렬