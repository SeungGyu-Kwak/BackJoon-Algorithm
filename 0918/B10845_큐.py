import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
  order= input().strip()
  # print(order)
  if "push" in order:
    order, n = order.split(" ")
    queue.append(n)
  elif order == "front":
    if len(queue) != 0:
      print(queue[0])
    else:
      print(-1)
  elif order == "back":
    if len(queue) != 0:
      print(queue[-1])
    else:
      print(-1)
  elif order == "pop":
    if len(queue) != 0:
      now = queue.popleft()
      print(now)
    else:
      print(-1)
  elif order == "size":
    print(len(queue))
  else:
    if len(queue) == 0:
      print(1)
    else:
      print(0)
    