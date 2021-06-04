import sys
from collections import deque
if __name__ == '___main__':
    n,m = list(map(int,sys. readline().split(" ")))
    arr = list()
    for i in range (m):
        arr.append(list(map(int,list(sys.readline().rstrip()))))
    visited = [[0 for i in range(n)] for j in range(m)]

    dir = [[1,0],[0,1],[-1,0],[0,-1]]
    dq = deque
    dq.append([0,0,0]) # 초기 출발값을 넣어준다
    while len (dq) > 0:
        cur_loc = dq. popleft
        x = cur_loc[0]
        y = cur_loc[1]
        sum = cur_loc[2]
        if x == m-1 and y == n-1:
            print(sum)
            break
        for d in dir:
            nx = x + d[0]
            ny = y + d[1]
            if nx >= m or ny >= n or nx < 0 or ny < 0:
                continue
            if visited[nx][ny] == 1:
                continue
            visited[nx][ny] = 1
            if arr[nx][ny] == 1 : # 부숴야하는 벽일 경우
                dq.append([nx,ny,sum+1])
            else:
                dq.appendleft([nx,ny,sum])