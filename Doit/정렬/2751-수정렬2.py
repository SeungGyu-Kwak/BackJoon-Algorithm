# 수 정렬하기 2
# 병합정렬
import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

N = int(input())
def mergeSort(s, e):
  if e - s < 1: return
  m = int(s + (e-s) / 2) # 중간점
  mergeSort(s, m)
  mergeSort(m+1, e)

  for i in range(s, e+1):
    tmp[i] = A[i]
  
  k = s
  index1 = s
  index2 = m + 1

  while index1 <= m and index2 <= e:
    if tmp[index1] > tmp[index2]:
      A[k] = tmp[index2]
      k += 1
      index2 += 1
    else:
      A[k] = tmp[index1]
      k += 1
      index1 += 1
  while index1 <= m: # 한쪽 그룹이 모두 선택된 후, 남아있는 값 정리
    A[k] = tmp[index1]
    k += 1
    index1 += 1
  while index2 <= e:
    A[k] = tmp[index2]
    k += 1
    index2 += 1

# 변수 선언
A = [0] * (N+1)
tmp = [0] * (N+1)

for i in range(1, N+1):
  A[i]  = int(input())

mergeSort(1, N)

for i in range(1, N+1):
  print(str(A[i]))

