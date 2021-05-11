import sys
def do_knapsack(item,value,weight,size):
    n = len(item)
    opt = [[0 for x in range(size+1)]for y in range(n+1)]
    for i in range(n+1):
        for w in range(size+1):
            # if i=0 -> 0
            if i == 0 or w == 0:
                opt[i][w] = 0
            elif weight[i-1] > w:
                opt[i][w] = opt[i-1][w]
            else:
                opt[i][w] = max(value[i-1] + opt[i-1][w-weight[i-1]], opt[i-1][w])
    return opt[len(opt)-1][len(opt[0])-1]
item = []
value = []
weight = []
n,k = list(map(int,sys.stdin.readline().split(" ")))
for i in range(n):
    ar = list(map(int,sys.stdin.readline().split(" ")))
    item.append(i)
    weight.append(ar[0])
    value.append(ar[1])
print(ar)
print(do_knapsack(item,value,weight,k))