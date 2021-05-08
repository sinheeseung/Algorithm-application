if __name__ == '__main__':
    n,m = map(int,input().split(" "))
    arr = list(map(int,input().split(" ")))
    arr.sort()
    # 이분 탐색을 위해 정렬
    start = 1
    # 가장 적게 걸리는 경우(최선의 케이스)
    end = max(arr) * n
    # 가장 오래걸리는 경우 (최악의 케이스)

    while start <= end:
        mid = (start + end) // 2
        count = 0
        for time in arr:
            count += mid // time
            # mid 시간으로 계산할 수 있는 인원 수 구함
            if count >= m:
                # mid 시간으로 모든 인원 계산 가능한 경우
                answer = mid
                end = mid - 1
                # 최소 시간을 줄여줌
                break
        if count < m:
            #모든 인원 계산 불가능한 경우
            start = mid + 1
            #최소 시간을 늘려줌
    print(answer)




