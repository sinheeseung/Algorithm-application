import sys

print("반복 횟수를 입력하세요")
n = int(sys.stdin.readline()) # 반복 횟수를 입력 받음
for i in range(n): # n만큼 반복
    sum = 0  # 입력받은 문자열의 총 점수를 저장하는 변수
    cnt = 0  # 문자열에서 각 A의 점수를 저장하는 번수
    print("문자열을 입력하세요")
    a = list(sys.stdin.readline())  # 문자열 입력 받음
    for j in range(len(a)-1): # 문자열의 길이만큼 반복
        if a[j] == 'A':  # 문자열의 j번째 문자가 'A'인 경우
            cnt = cnt + 1  # A인 경우 점수를 1 더해줌
            sum = sum + cnt # 구한 점수를 총 점수에 더해줌
        else:
            cnt = 0 # 'A'의 연속이 끝기면 0으로 초기화
    print(sum) # 총 점수를 출력
print("프로그램을 종료합니다.")

