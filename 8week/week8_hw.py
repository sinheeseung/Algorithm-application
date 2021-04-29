import sys
import functools

def comparator(x,y):
    #x가 뒤에있는 숫자, y가 앞에있는 숫자
    num_1 = x + y
    #x가 앞부분에 왔을 경우의 숫자
    num_2 = y + x
    #y가 앞부분에 왔을 경우의 숫자
    return int(num_2) - int(num_1)
    # 가장 큰 수를 구해야 하기 때문에
    # num_2가 더 크면 양수 return, num_1이 더 크면 음수 return
    # 음수가 return 되면 순서가 바뀜


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    arr = list(map(str, input().split(" ")))
    arr.sort(key = functools.cmp_to_key(comparator))
    #comparator 함수로 정렬 조건을 정해줌
    for i in range(n):
        print(arr[i], end='')

