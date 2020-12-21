def waterArea(heights):

    maxes = [0 for _ in heights]
    leftMax = 0

    for i in range(len(heights)):
        maxes[i] = leftMax
        leftMax = max(leftMax, heights[i])
    
    rightMax = 0
    waterArea = 0
    for i in reversed(range(len(heights))):
        minHeight = min(rightMax, maxes[i])
        if heights[i] < minHeight:
            maxes[i] = minHeight - heights[i]
        else:
            maxes[i] = 0
        rightMax = max(rightMax, heights[i])
        waterArea += maxes[i]

    return waterArea

print(waterArea([0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]))

