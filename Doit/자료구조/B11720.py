import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
list_a = list(map(int, input()))

print(sum(list_a))