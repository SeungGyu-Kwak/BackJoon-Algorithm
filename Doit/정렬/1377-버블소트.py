# 버블소트
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

# 값 입력받기
N = int(input())
ary = []
for i in range(N):
  ary.append((int(input()), i))


# 정렬하기 전 각자의 인덱스 추출
sorted_ary = sorted(ary)# 오름차순으로 정렬 (O(NlogN))
result = [] # 전과 후의 인덱스 차이를 담을 리스트

Max = 0
for i in range(N):
  if Max < sorted_ary[i][1] - i:
    Max = sorted_ary[i][1] - i

print(Max + 1)

