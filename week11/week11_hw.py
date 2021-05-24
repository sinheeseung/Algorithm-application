import sys
import collections

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
dr = ['U', 'D', 'L', 'R']

def min_count(block, m,n):
    q = collections.deque([(0, 0, 0)])
    # x좌표, y좌표, (x,y)에 도달하기 위해 바꾼경로의 갯수
    ans = 10000
    visited = [[int(10000)] * n for _ in range(m)]
    # x,y좌표에 도달하기 위해 바꾼경로의 갯수 저장
    visited[0][0] = 0

    while q:
        x, y, count = q.popleft()
        if x == m - 1 and y == n - 1:
            # m-1, n-1 까지 가는데 필요한 바꾼경로의
            # 최단거리를 구해줌
            ans = min(ans, count)
            continue
            # m-1, n-1 좌표인 경우 이동 할 필요가 없으므로 continue
        for i in range(4):
            # 이동 할 수 있는 4방향 상, 하, 좌, 우
            nx, ny = x + dx[i], y + dy[i]
            cnt = count
            if 0 <= nx < m and 0 <= ny < n:
                # 범위 내인 경우
                if block[x][y] != dr[i]:
                    # 이동방향과 문자가 달라 경로를 바꿔야 하는 경우
                    cnt += 1
                    # 횟수추가
                if visited[nx][ny] > cnt:
                    # nx,ny까지 가는데 필요한 바꾼 경로가 기존보다 작은 경우
                    q.append((nx, ny, cnt))
                    visited[nx][ny] = cnt
                    # 좌표까지 필요한 바꾼 횟수 수정

    return ans

m, n = map(int, input().split())
block = [list(input().split()) for _ in range(n)]
print(min_count(block,m,n))