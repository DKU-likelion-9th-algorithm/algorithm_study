# https://www.acmicpc.net/problem/1655

import sys
import heapq

input = sys.stdin.readline

N = int(input())
num_list = []

'''
for _ in range(N):
    num_list.append(int(input()))
    num_list.sort()
    if len(num_list) % 2 != 0:
        print(num_list[len(num_list)//2])
    else:
        print(num_list[(len(num_list)//2)-1])
'''

for i in range(N):
    num = int(input())
    heapq.heappush(num_list, num)
    if len(num_list) % 2 != 0:
        print(num_list[len(num_list)//2])
    else:
        print(num_list[(len(num_list)//2)-1])
