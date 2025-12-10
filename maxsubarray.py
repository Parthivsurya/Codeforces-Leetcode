arr=[1,2,3,4,3,4,5,6,7,8,9]
for i in range(len(arr)-1):
    if arr[i] < arr[i+1]:
        print("Increasing")
    elif arr[i] > arr[i+1]:
        print("Decreasing")
    else:
        print("Equal")
print("End of array")
output should be 1 2 3 4 5 6 7 8 9
