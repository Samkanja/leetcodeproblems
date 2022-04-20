def minimumSizeArraySum(arr,target):
    totalSum=i= k= 0
    res = float('inf')
    while i < len(arr):
        totalSum += arr[i]
        while totalSum >= target:
            res = min(i - k +1, res)
            totalSum -= arr[k]
            k += 1
        i += 1
    return 0 if res == float('inf') else res

nums = [2,3,1,2,4,3]
print(minimumSizeArraySum(nums, 7))
 