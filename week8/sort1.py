n = int(input())
data = list(map(int, input().split()))
data.sort()
print(data[(n - 1) // 2]) # 중간값(median)을 출력