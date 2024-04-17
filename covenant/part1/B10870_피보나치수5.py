import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline



N = int(input())
def Fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return Fibo(n-1) + Fibo(n-2)

result = Fibo(N)
print(result)

arr = [[0]* 3 for _ in range(5)]
print(arr)

