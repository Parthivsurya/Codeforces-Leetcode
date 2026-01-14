def largestno(arr):
        radixarr = [[] for _ in range(10)]
        exp=1
        for i in range(1):
            for val in arr:
                radixindex=(val//exp)%10
                radixarr[radixindex].append(val)
            arr=[]
            for bucket in radixarr:
                for val in bucket:
                    arr.append(val)
                bucket.clear()
            exp*=10
        result = ''.join(map(str, arr[::-1]))
        return result
arr=[10,2]
largestno(arr)