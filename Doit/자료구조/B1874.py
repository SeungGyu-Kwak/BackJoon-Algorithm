import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())

A = []
for i in range(N):
  tmp = int(input())
  A.append(tmp)

stack = [] # 스택
num = 1
answer = ""
result = True
for i in range(N):
  s = A[i]
  if s >= num:
    while s >= num:
      stack.append(num)
      num += 1
      answer += "+\n"
    stack.pop()
    answer += "-\n"
  else:
    n = stack.pop()
    if n > s:
      print("NO")
      result = False
      break
    else:
      answer += "-\n"

if result:
  print(answer)
      
  