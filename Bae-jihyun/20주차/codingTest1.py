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

'''
단순 최대 차이

증권 연구에서 분석가는 주식의 여러 속성을 살펴봅니다. 한 분석가는 역사상 전일 종가와 종가 사이의 가장 높은 양의 스프레드를 기록하고 싶어합니다. 
가격 이력이 주어진 주식의 최대 양의 스프레드를 결정합니다. 주식이 전체기간 동안 평평하게 유지되거나 하락하면 -1을 반환합니다.

예) 
px = [7, 1, 2, 5]
첫 번째 7은 그 이전의 비교할 가격이 없습니다.
두 번째 1은 더 낮은 이전 가격이 없습니다.
세 번째 2는 그 이전 가격인 1보다 높습니다. 2-1 = 1
네 번째 5는 그 이전 가격인 1, 2보다 높습니다. 5-1 = 4
                                       5-2 = 3
최대 차이는 4입니다.
'''