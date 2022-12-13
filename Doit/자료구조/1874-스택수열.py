# 스택 수열
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
stack = [] # 스택 생성
num = 1
answer = ''
isTrue = True
for n in range(N):
  value = int(input())

  if num <= value:
    while num <= value:
      stack.append(num)
      num += 1
      answer += '+\n'
    stack.pop()
    answer += '-\n'
  else:
    a = stack.pop()
    if a > value:
      print('No')
      isTrue = False
      break
    else:
      answer += '-\n'

if isTrue:
  print(answer)