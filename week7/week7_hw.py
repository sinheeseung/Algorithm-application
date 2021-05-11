from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

#섬마다 번호로 mapping해줌
def bfs1(x, y, cnt):
    q.append([x, y])
    map_is[x][y] = cnt
    while q:
        #쿠가 빌 때까지 반복
        x, y = q.popleft()
        for i in range(4):
            #상,하,좌,우 이동
            x2 = x + dx[i]
            y2 = y + dy[i]
            if 0 <= x2 < n and 0 <= y2 < n:
            #범위 내에 있는 경우
                if island[x2][y2] == 1 and map_is[x2][y2] == 0:
                    #섬이고 아직 번호가 없는 경우
                    map_is[x2][y2] = cnt
                    #섬의 번호 지정
                    q.append([x2, y2])

#섬 간 이동거리를 구함
def bfs2(num):
    while q2:
        #큐가 빌 때까지 반복
        x, y = q2.popleft()
        for i in range(4):
            #상,하,좌,우 이동
            x2 = x + dx[i]
            y2 = y + dy[i]
            if 0 <= x2 < n and 0 <= y2 < n:
            # 범위 내에 있는 경우
                if island[x2][y2] == 1 and map_is[x2][y2] != num:
                    #num로 mapping된 섬과 다른 섬을 만난 경우
                    return c2[x][y]-1
                if island[x2][y2] == 0 and c2[x2][y2] == 0:
                    #아직 방문하지 않은 바다인 경우
                    c2[x2][y2] = c2[x][y] + 1
                    q2.append([x2, y2])

n = int(sys.stdin.readline())
island = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
map_is = [[0]*n for _ in range(n)]
#섬 마다 번호를 다르게 mapping한 배열
q = deque()
cnt = 1

for i in range(n):
    for j in range(n):
        if island[i][j] == 1 and map_is[i][j] == 0:
            bfs1(i, j, cnt)
            cnt += 1
            #cnt번째에 mapping되지 않은 섬은
            #연결되지 않은 섬이다.
a = n*n
#최댓값
for k in range(1, cnt):
    #섬의 개수만큼 반복
    q2 = deque()
    c2 = [[0] * n for _ in range(n)]
    #cnt번째 섬에서 가장 가까운 섬 까지의 이동거리를 구함
    for i in range(n):
        for j in range(n):
            if island[i][j] == 1 and map_is[i][j] == k:
                #cnt번째 섬을 1로 mapping해주고 queue에 넣음
                q2.append([i, j])
                c2[i][j] = 1
    res = bfs2(k)
    #k번째 섬이 포함 된 경우 최소 거리
    a = min(a, res)
    #최소 거리 중 최솟값을 구함
print(a)