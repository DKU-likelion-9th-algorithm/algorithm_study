# https://www.acmicpc.net/problem/2331
import sys

input = sys.stdin.readline

A, P = map(int, input().split())
nums = [A]
j = 0

while True:
    num = []
    for i in str(nums[j]):
        num.append(int(i)**P)
    if sum(num) in nums:
        index = nums.index(sum(num))
        for k in range(len(nums)-1, index-1, -1):
            del nums[k]
        break
    else:

        nums.append(sum(num))
    j += 1

print(len(nums))
