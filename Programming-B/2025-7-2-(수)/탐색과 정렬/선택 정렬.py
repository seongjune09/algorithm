def sel_sort(a):
    n = len(a)
    for i in range(0, n-2):
        min_idx = i
        for j in range(i+1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i],a[min_idx] = a[min_idx],a[i]
    return a
            
d = [2,4,5,1,3]
sel_sort(d)
print(d)
