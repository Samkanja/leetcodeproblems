def totalFruit(fruits):
    i=k=maxLen=0
    d = {}
    while i < len(fruits):
        d[fruits[i]] = i
        if len(d) >= 3:
            minVal = min(d.values())
            del d[fruits[minVal]]
            k = minVal + 1
        maxLen = max(maxLen, i - k +1)
        i += 1
    return maxLen
fruits = [2,1,2,3,2]
print(totalFruit(fruits))