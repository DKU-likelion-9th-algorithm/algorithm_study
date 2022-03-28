# https://www.acmicpc.net/problem/1764

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
Nset = set()
Mset = set()

for _ in range(N):
    Nset.add(input())
for _ in range(M):
    Mset.add(input())

result = sorted(Nset.intersection(Mset))  # 교집합

print(len(result))
print(''.join(result), end='')
