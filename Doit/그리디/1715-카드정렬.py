# 카드 정렬하기
import sys
from queue import PriorityQueue
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
queue = PriorityQueue() # 우선순위 큐 생성
for i in range(N):
  a = int(input())
  queue.put(a) # 값 입력 받고 우선순위 큐에 넣기

data1 = 0
data2 = 0
sum = 0
while queue.qsize() > 1:
  data1 = queue.get()
  data2 = queue.get()
  tmp = data1 + data2
  sum += tmp
  queue.put(tmp)

print(sum)

