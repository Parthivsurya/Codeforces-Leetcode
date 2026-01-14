myarray=[170,45,75,90,802,24,2,66]
print("Unsorted array:",myarray)
def radixsort(arr):
    radixarr = [[] for _ in range(10)]
    max1=max(arr)
    exp=1
    while max1//exp>0:
        for val in arr:
            radexindex=(val//exp)%10
            radixarr[radexindex].append(val)
        arr=[]
        for bucket in radixarr:
            for val in bucket:
                arr.append(val)
            bucket.clear()
        exp*=10
    return arr
sortedarray=radixsort(myarray)
print("Sorted array:",sortedarray)