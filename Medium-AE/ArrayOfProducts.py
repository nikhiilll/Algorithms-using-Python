def arrayOfProducts(array):
    """
    TC: O(n^2) | SC: O(n)
    """
    n = len(array)
    result = []
    for i in range(n):

        leftProduct, rightProduct = 1, 1
        left, right = i -1, i + 1

        while left >= 0:
            leftProduct *= array[left]
            left -= 1
        
        while right < n:
            rightProduct *= array[right]
            right += 1
        
        result.append(leftProduct * rightProduct)
    
    return result

def arrayOfProducts2(array):
    """
    TC: O(n) | SC: O(n)
    """
    result = [1] * len(array)
    leftProducts = [1] * len(array)
    rightProducts = [1] * len(array)

    leftRunningProduct = 1
    for i in range(len(array)):
        leftProducts[i] = leftRunningProduct
        leftRunningProduct *= array[i]
    
    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        rightProducts[i] = rightRunningProduct
        rightRunningProduct *= array[i]
    
    for i in range(len(array)):
        result[i] = leftProducts[i] * rightProducts[i]
    
    return result


    

print(arrayOfProducts2([5, 1, 4, 2]))

