# 좋다
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort() # 정렬

Result = 0
for k in range(N):
    find = A[k]
    i = 0 #start index
    j = N - 1 # end index
    
    while i < j: # 투포인터 알고리즘
        if A[i] + A[j] == find:
            if i != k and j != k:
                Result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif A[i] + A[j] < find:
            i += 1
        else:
            j -= 1

print(Result)


