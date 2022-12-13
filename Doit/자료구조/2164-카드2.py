# 카드 2
import sys
from collections import deque
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 변수 선언
N = int(input())
myQueue = deque()

# 큐에 값 넣기
for i in range(1, N+1):
  myQueue.append(i)

while len(myQueue) != 1:
  myQueue.popleft() # 큐 맨 앞에 있는 값 버리기
  value = myQueue.popleft() # 그 다음 값 뽑아서 큐 맨 뒤로 넣기
  myQueue.append(value)

print(myQueue[0]) # 큐에 한개만 남으면 해당 값 출력


