import sys
def TSP(cur_loc,visited):
    ret = dp[cur_loc][visited]
    if ret != 0:
        return ret
    if visited==((1<<n)-1):
        if arr[cur_loc][0] != 0:
            return arr[cur_loc][0]
        else:
            return sys.maxsize
    ret = sys.maxsize
    for i in range (n):
        if arr[cur_loc][i]== 0 or visited & (1<<i):
            continue
        ret = min(ret,arr[cur_loc][i] + TSP(i,visited|1<<i))
    dp[cur_loc][visited] = ret

    return ret
if __name__ == '__main__':
    n = int(sys.stdin.readline())
    arr = list
    dp = [[0 for i in range (1<<n)] for j in range (n)]
    for i in range (n):
        arr.append(list(map(int,sys.readlinesplit(" "))))
    print(TSP(0,1))