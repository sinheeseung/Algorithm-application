import sys

if __name__ == '__main__':
    input_num = int(sys.stdin.readline())
    arr = [[0 for _ in range(2)] for _ in range(input_num)]
    for i in range(input_num):
        a,b = input().split(" ")
        arr[i][0] = int(a)
        arr[i][1] = int(b)
    arr.sort()
    # 내장되어 있는 정렬 사용 시간복잡도 : nlogn
    # a과목을 기준으로 정렬
    min = arr[0][1]
    # 탐색한 사람들 중에서 b과목의 최소 등수 저장
    cnt = 1
    # a과목이 1등인 사람은 무조건 대표가 되므로 1에서 시작
    for i in range(1, input_num):
        # a과목 2등부터 꼴등까지 탐색 시간복잡도 : n-1
        if(arr[i][1] < min):
            # a과목 등수로 정렬되어 있기 때문에 i번째 사람이 대표가 되기
            # 위해서는 자기보다 위에 있는 사람들과 b 과목만 비교하면 된다.
            # 따라서 탐색한 사람들 중에서 b과목의 최소 등수인 min보다 b과목 등수가 작다면
            # 자신보다 a과목을 잘본 사람 전부보다 잘 본것이기 때문에
            # 대표선수로 선발되게 된다.
            min = arr[i][1]
            # 대표선수로 선발된 경우는 b과목 등수가 탐색을 진행한 사람들 중에
            # 가장 작다는 뜻이기 때문에 min값을 새로 정해준다.
            cnt += 1
    print(cnt)


