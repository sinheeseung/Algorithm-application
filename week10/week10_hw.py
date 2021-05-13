import sys
def calc(n,price,carlorie,size):
    opt = [[0 for x in range (size+1)]for y in range(n+1)]
    for i in range(n+1):
        for w in range(size+1):
            # if i=0 -> 0
            if i == 0 or w == 0:
                opt[i][w] = 0
            elif price[i - 1] > w:  # 제품의 가격이 더 큰 경우
                opt[i][w] = opt[i - 1][w]
            else:
                opt[i][w] = max(opt[i - 1][w], opt[i][w - price[i - 1]] + carlorie[i - 1])
                #중복이 가능하기 때문에 opt배열에서 [i-1]이 아니라 [i]사용
    return opt[len(opt)-1][len(opt[0])-1]

price = []
carlorie = []
n,m = sys.stdin.readline().split(" ")
n = int(n)
m = int(float(m) * 100)
#소수점이 2자리로 고정이기 때문에 *100해서 정수값 사용
for i in range(int(n)):
    p,c = list(map(float,sys.stdin.readline().split(" ")))
    price.append(int(p*100))
    carlorie.append(int(c))

print(calc(n,price,carlorie,m))




