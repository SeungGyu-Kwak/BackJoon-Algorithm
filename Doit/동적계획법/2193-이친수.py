import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

S = [0] * 91
S[1] = 1
S[2] = 1

for i in range(3, 91):
    S[i] = S[i-1] + S[i-2]

N = int(input())
print(S[N])