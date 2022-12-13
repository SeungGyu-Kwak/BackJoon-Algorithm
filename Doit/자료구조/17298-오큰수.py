# 오큰수
# Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미
# 그러한 수가 없는 경우에 오큰수는 -1이다.

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
# 값 입력받기
N = int(input())
ary = list(map(int, input().split()))
print('test입니다')
# 변수 선언
result = [0] * N # 오큰 수 담을 리스트
stack = [] # 스택

for i in range(N):
  while stack and ary[stack[-1]] < ary[i]:
    result[stack.pop()] = ary[i]
  stack.append(i)

while stack: # 반복문을 다돌고 나왔는데 스택에 값이 있으면
  result[stack.pop()] = -1

for i in result:
  print(str(i), end = ' ')
