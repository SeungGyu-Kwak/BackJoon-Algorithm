import sys
import math
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

s = int(input())
e = int(input())

primeList = []

for num in range(s, e+1):
    isPrime = False
    if num > 1:
        for i in range(2, num-1):
            if num % i == 0:
                isPrime = True
        if not isPrime:
            primeList.append(num)

print(sum(primeList))
print(min(primeList))

        
