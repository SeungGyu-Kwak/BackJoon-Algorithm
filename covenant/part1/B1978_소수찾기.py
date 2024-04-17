import sys
import math
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
ary = list(map(int, input().split()))

result = 0
for x in ary:
    isPrime = True
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                isPrime = False
                break
        if isPrime:
            result += 1

print(result)
            


# 소수찾기 (에라토스테네스의 체 알고리즘 사용하는 것도 있음)
# 소수의 범위만큼 1차원리스트 생성
# 2부터 시작. 현재 숫자가 지워진 상태가 아닌경우 선택된
# 숫자의 배수를 리스트에서 다 삭제.
# 이때, 처음 선택된 수는 삭제 x
# 2부터 N의 제곱근 까지만 탐색 int(math.sqrt(N))



