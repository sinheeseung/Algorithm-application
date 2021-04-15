import sys


def calc_loc(next_loc, loc):
    #지렁이의 이동방향 계산
    if (loc == 'R' and next_loc == 'R'):
        #지렁이가 오른쪽으로 가고 있을 때 다음 방향이 오른쪽인 경우
        loc = 'D'
    elif (loc == 'R' and next_loc == 'L'):
        #지렁이가 오른쪽으로 가고 있을 때 다음 방향이 왼쪽인 경우
        loc = 'U'
    elif (loc == 'L' and next_loc == 'R'):
        #지렁이가 왼쪽으로 가고 있을 때 다음 방향이 오른쪽인 경우
        loc = 'U'
    elif (loc == 'L' and next_loc == 'L'):
        #지렁이가 왼쪽으로 가고 있을 때 다음 방향이 왼쪽인 경우
        loc = 'D'
    elif (loc == 'U' and next_loc == 'R'):
        #지렁이가 위쪽으로 가고 있을 때 다음 방향이 오른쪽인 경우
        loc = 'R'
    elif (loc == 'U' and next_loc == 'L'):
        #지렁이가 위쪽으로 가고 있을 때 다음 방향이 왼쪽인 경우
        loc = 'L'
    elif (loc == 'D' and next_loc == 'R'):
        #지렁이가 아래쪽으로 가고 있을 때 다음 방향이 오른쪽인 경우
        loc = 'L'
    elif (loc == 'D' and next_loc == 'L'):
        #지렁이가 아래쪽으로 가고 있을 때 다음 방향이 왼쪽인 경우
        loc = 'R'
    return loc

def move(x,y,loc):
    #지렁이 머리의 다음 좌표 계산
    if (loc == 'R'):
        #오른쪽으로 이동이면 y + 1
        y += 1
    elif (loc == 'L'):
        #왼쪽으로 이동이면 y - 1
        y -= 1
    elif (loc == 'U'):
        #위쪽으로 이동이면 x - 1
        x -= 1
    elif (loc == 'D'):
        #아래쪽으로 이동이면 x + 1
        x += 1
    return x,y

if __name__ == '__main__':
    n = int(sys.stdin.readline()) #판의 크기
    k = int(sys.stdin.readline()) # 사과의 개수
    m = int(sys.stdin.readline()) #방향 전환 횟수
    arr = [[0 for _ in range(n)] for _ in range(n)]  #판
    #빈칸은 0으로 채우고, 지렁이는 1의 값으로, 먹이는 2의 값으로 설정
    dic = {}
    #방향 전환에 대한 정보 저장
    for i in range(k):
        a,b = input().split(" ")
        arr[int(a)-1][int(b)-1] = 2
    for i in range(m):
        a,b = input().split(" ")
        dic[int(a)] = b
    loc = 'R';  arr[0][0] = 1
    #지렁이의 시작 위치와 시작방향 설정
    count = 0; x = 0; y = 0; a = 0
    # count : Turn을 저장하는 변수
    # x,y : 지렁이 머리의 위치
    queue_x = list(); queue_y = list()
    #지렁이의 이동위치를 저장

    while(1):
        queue_x.append(x)
        queue_y.append(y)
        #지렁이의 이동위치를 저장
        if(count in dic):
            #이번 Trun에 방향전환이 일어나야 하는 경우
            next_loc = dic.get(count)
            #사전에서 현재 Trun을 key값으로 가지는 방향을 가져옴
            loc = calc_loc(next_loc,loc)
            #calc_loc함수를 통해 다음 이동 방향을 계산
        x,y = move(x,y,loc)
        #move함수를 통해 다음 지렁이 머리의 위치를 계산
        count+=1
        #turn증가
        if(x >= n or y >= n or x < 0 or y < 0):
            #지렁이가 판 밖으로 나가는 경우 프로그램 종료
            break
        if(arr[x][y] == 2):
            #지렁이가 먹이를 먹은 경우
            arr[x][y] = 1
            #길이가 늘어나기 때문에 꼬리를 지워주지 않음
        elif(arr[x][y] == 1):
            #지렁이가 자신의 몸과 부딪혀서 프로그램 종료
            break
        else:
            #지렁이가 앞으로 이동했기 때문에 꼬리를 지워줌
            #꼬리를 지우기 위해 가장 먼저 입력된 값의 위치를 0으로 지정
            arr[x][y] = 1
            arr[queue_x.pop(0)][queue_y.pop(0)] = 0
    print(count)