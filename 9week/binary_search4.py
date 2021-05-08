def peakIndexInMountainArray(list):
    lo, hi= 0, len(list)-1
    while lo < hi:
        mi = int((lo + hi) // 2)
        if(list[mi] < list[mi+1]):
            lo = mi + 1
        else:
            hi = mi
    return lo

list = [3,4,5,1]

answer = peakIndexInMountainArray(list)
print(answer)