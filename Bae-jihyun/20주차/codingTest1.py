import sys
input = sys.stdin.readline


def max_difference(lst):
    result = -1
    min_index, max_index = None, None

    # min_index, max_index 찾기
    for index, value in enumerate(lst):
        if min_index is None or value < lst[min_index]:
            min_index = index
        if max_index is None or value > lst[max_index]:
            max_index = index
            if max_index > min_index:  # 만약 max_index가 min_index보다 크면
                result = max(result, lst[max_index]-lst[min_index])  # result와 두 값의 차이 중 더 큰 값으로 result 갱신

    # 4 5 2 4와 같이 max_index =1, min_index = 2이면 result = 1이다.
    # 하지만 가장 큰 차이(result)는 max_index = 3, min_index = 2, lst[3]-lst[2]일때인 = 2일 떄이기 때문에
    # min_index를 이용해 다시 한번 계산해줌
    for i in range(min_index+1, len(lst)):
        diff = lst[i]-lst[min_index]
        if diff > result:
            result = diff

    # lst 인덱스가 커질수록 값이 계속 유지되거나 떨어지면 result는 0이 되지만 -1을 출력해야 한다.
    print(result if result != 0 else -1)


n = int(input())
px = []
for _ in range(n):
    px.append(int(input()))

max_difference(px)
