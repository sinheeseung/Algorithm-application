import re
import sys
import math
from itertools import permutations


def only_nature():
    # 자연수만 얻고 싶기때문에 only_nature 사용
    return re.compile("[0-9]+")


def is_prime(num):
    # 소수인지 확인하는 함수
    for k in range(2, int(math.sqrt(num)) + 1):
        # 에라토스테네스의 채를 통해 제곱근 까지만 확인해보면 소수인지 판별 가능
        if num % k == 0:
            return False
    return True


if __name__ == '__main__':
    compile1 = only_nature()
    input_num = int(sys.stdin.readline())
    arr_list = list()
    # 입력받은 숫자를 한 자리수 단위로 끊어 저장한 배열
    input_list = list()
    # 입력받은 숫자로 만들 수 있는 수의 list
    p_list = list()
    # 입력받은 숫자중 i개의 원소로 만들 수 있는 수 들의 list
    int_list = list()
    # 정규표현식을 통해 추출된 만들 수 있는 수 들의 list
    cnt = 0
    while input_num > 0:
        arr_list.append(input_num % 10)
        input_num = int(input_num / 10)
        # 입력받은 숫자에서 한 자리수 단위로 끊어 arr_list에 저장
    for i in range(len(arr_list)):
        p = permutations(arr_list, i+1)
        # arr_list의 원소들 중에서 i개의 원소를 가지는 순열을 만듬
        p_list = list(p)
        for j in range(len(p_list)):
            input_list.append(str(list(p_list[j])).replace(', ', ''))
            # permutations 함수를 사용하면 ', '로 원소들이 구분되기 때문에 replace를 통해 삭제해줌
    for j in range(len(input_list)):
        int_list.append(compile1.search(input_list[j]).group())
        int_list[j] = int(int_list[j])
        # permutations 함수를 통해 만들어진 순열 list에서 정규표현식을 이용해
        # 숫자만 분리하여 자료형을 int로 바꿔줌
    int_list = list(set(int_list))
    # list에서 중복된 원소를 제거해 줌
    int_list.sort()
    for j in range(len(int_list)):
        if int_list[j] > 1:
            # 1은 소수가 아님
            if is_prime(int_list[j]):
                # 소수인 경우 count
                cnt += 1
    print(cnt)
