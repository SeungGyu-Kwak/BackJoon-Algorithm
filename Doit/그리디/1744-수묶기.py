# 수 묶기
import sys
from queue import PriorityQueue
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 우선순위 큐 생성
pluspq = PriorityQueue() # 1보다 큰 양수 담을 큐
minuspq = PriorityQueue() # 음수를 담을 큐
zero = 0 # 0 개수
one = 0 # 1 개수
sum = 0 # 더한 값 변수

N = int(input()) # 수열의 크기
# 각 큐에 담기
for i in range(N):
  data = int(input())
  if data == 0:
    zero += 1
  elif data == 1:
    one += 1
  elif data > 1:
    pluspq.put(data * -1) # 내림차순으로 정렬하기 위해 -1곱해서 저장
  else:
    minuspq.put(data)

# 양수 우선순위큐 처리
while pluspq.qsize() >= 2:
  tmp1 = pluspq.get() * -1
  tmp2 = pluspq.get() * -1
  sum += tmp1 * tmp2 

# 양수 우선순위 큐에 남았는 값 처리
if pluspq.qsize() > 0:
  sum += pluspq.get() * -1

# 음수 우선순위큐 처리
while minuspq.qsize() >= 2:
  tmp1 = minuspq.get()
  tmp2 = minuspq.get()
  sum += tmp1 * tmp2

# 음수 우선순위 큐에 남았는 값 처리
if minuspq.qsize() > 0:
  if zero == 0:
    sum += minuspq.get()

# 전체 결과 , 1 남은 만큼 더하기
sum += one

print(sum)

