import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    board = list(map(int, input().split()))
    _min = 200000000
    left, right = 0, len(board)-1

    board.sort()

    while left < right:
        s = board[left] + board[right]
        if s < k:
            left += 1
        if s >= k:
            right -= 1

        if abs(k - s) < _min:
            cnt = 1
            _min = abs(k - s)
        elif abs(k - s) == _min:
            cnt += 1

    print(cnt)


'''
투포인터를 활용하였고 abs를 사용해야 했다. (두 수의 합이 정해진 k와 가까운 조합의 개수 찾기) 
min을 저장하고 같은 절대 값이 생길경우 cnt를 증가시켜주는 것도 중요.

시간복잡도는 O(n)으로 충분히 통과 할 수 있을거라고 생각. [여기서 n은 1,000,000]
실제 테스트 돌렸을 땐 육안으로 확인가능할 정도로 너무 느렸음.
여기서 시간을 더 줄일 수 있는 방법은? 
'''