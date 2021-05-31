import collections
m, n = map(int, input().split())
block = [list(map(int,(input().split()))) for _ in range(m)]
visit = [[False]*n for _ in range(m)]
ans = [[0]*n for _ in range(m)]
q = collections.deque([])
for i in range(m):
    for j in range(n):
        q.append((block[i][j],i,j))
        # Queue에 삽입
q = sorted(q)
#입력값을 오름차순으로 정렬

while q:
    value,x,y = q.pop(0)
    #최솟값부터 진행\
    count_x = 1 #행에서의 순위
    count_y = 1 #열에서의 순위
    index_max = 0
    #바뀐 순위 행렬에서의 자신보다 작은 값이
    #가지고 있는 순위의 최댓값 저장
    equl_value = 0
    #행/열 내에서 같은 값이 있으면 그 때의 값 저장
    #check_row
    for i in range(n):
        # 최소값부터 진행하였기 때문에 방문한 좌표는 무조건 현재 좌표보다
        # 작거나 같은 값이 들어있다.
        if visit[x][i]:
            #현재 좌표에 있는 값보디 행에서 작은 값이 있는 경우
            if value == block[x][i]:
                #값이 같은 경우 순위도 같으므로 순위 저장
                equl_value = ans[x][i]
            count_x += 1
            index_max = max(ans[x][i],index_max)
            #행에서 index의 최대값 저장
    for i in range(m):
        if visit[i][y]:
            #현재 좌표에 있는 값보다 열에서 작은 값이 있는 경우
            if value == block[i][y]:
                #값이 같은 경우 순위도 같으므로 순위 저장
                equl_value = ans[i][y]
            count_y += 1
            index_max = max(ans[i][y],index_max)
            #행,열에서 index의 최대값 저장
    count_max = max(count_x,count_y)
    #행,열에서 순위를 구함
    if equl_value != 0:
        #같은 값이 있는 경우
        ans[x][y] = equl_value
        # 그 값의 순위와 같은 순위를 가짐
    elif(index_max != 0 and count_max<= index_max):
        #현재 좌표의 행,열에서의 최대 순위가 같은 행,열에 있는 자신보다 작은 값의
        #순위보다 작은경우
        ans[x][y] = index_max+1
        #행렬 최대 순위 +1값을 넣어줌
    else:
        ans[x][y] = count_max
    visit[x][y] = True
    #방문 check
for i in range(m):
    for j in range(n):
        print(ans[i][j], end = ' ')
    print()

'''4 3
20 -21 14
-19 4 19
22 -47 24
-19 4 19'''