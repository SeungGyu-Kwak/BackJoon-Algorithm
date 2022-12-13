# DNA 비밀번호
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 변수 선언
checkList = [0] * 4
myList = [0] * 4
checkSecret = 0 
result = 0

# myAdd 함수 설정
def myAdd(c):
  global checkSecret, myList, checkSecret

  if c == 'A':
    myList[0] += 1
    if checkList[0] == myList[0]:
      checkSecret += 1
  if c == 'C':
    myList[1] += 1
    if checkList[1] == myList[1]:
      checkSecret += 1
  if c == 'G':
    myList[2] += 1
    if checkList[2] == myList[2]:
      checkSecret += 1
  if c == 'T':
    myList[3] += 1
    if checkList[3] == myList[3]:
      checkSecret += 1

# myRemove 함수 설정
def myRemove(c):
  global checkSecret, myList, checkSecret

  if c == 'A':
    if checkList[0] == myList[0]:
      checkSecret -= 1
    myList[0] -= 1
  if c == 'C':
    if checkList[1] == myList[1]:
      checkSecret -= 1
    myList[1] -= 1
  if c == 'G':
    if checkList[2] == myList[2]:
      checkSecret -= 1
    myList[2] -= 1
  if c == 'T':
    if checkList[3] == myList[3]:
      checkSecret -= 1
    myList[3] -= 1


S, P = map(int, input().split())
DNA_string = list(input())
checkList = list(map(int, input().split()))

# 초기값 설정
for i in range(4):
  if checkList[i] == 0:
    checkSecret += 1

for i in range(P):
  myAdd(DNA_string[i])

if checkSecret == 4:
  result += 1

for i in range(P, S):
  j = i - P
  myAdd(DNA_string[i])
  myRemove(DNA_string[j])
  if checkSecret == 4:
    result += 1
print(result)



