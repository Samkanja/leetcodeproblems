def maximumAvarageSubArray(arr,k):
    maxSum = totalSum = sum(arr[:k])
    x = 0
    for i in range(k,len(arr)):
        totalSum += arr[k] - arr[x]
        maxSum = max(maxSum,totalSum)
        x += 1
    return maxSum/k

arr = [1,12,-5,7,0,4,8,2]
print(maximumAvarageSubArray(arr,4))