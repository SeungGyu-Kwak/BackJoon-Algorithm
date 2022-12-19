# 버블소트
# N이 500,000이라서 버블소트로 풀면 타인에러가 난다.
# 병합정렬로 푼다.

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
result = 0

# 병합정렬 함수
def mergeSort(s,e):
  global result
  if e - s < 1: return
  m = int(s + (e - s)/2)
  mergeSort(s, m)
  mergeSort(m+1, e)

  for i in range(s, e+1):
    tmp[i] = A[i]
  k = s
  index1 = s
  index2 = m+1
  while index1 <= m and index2 <= e:
    if tmp[index1] > tmp[index2]:
      A[k] = tmp[index2]
      result = result + index2 - k
      k += 1
      index2 += 1
    else:
      A[k] = tmp[index1]
      k += 1
      index1 += 1
  while index1 <= m:
    A[k] = tmp[index1]
    index1 += 1
    k += 1
  while index2 <= e:
    A[k] = tmp[index2]
    index2 += 1
    k += 1

# 변수 선언
N = int(input())
A = list(map(int, input().split()))
A.insert(0, 0) # 0인덱스는 사용하지 않기 위해 0에 0을 넣음
tmp = [0] * (N+1)

mergeSort(1, N)
print(result) 