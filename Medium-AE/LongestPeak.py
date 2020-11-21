def longestPeak(array):

    longestPeak = 0

    if len(array) <= 2:
        return longestPeak
    
    current, previous = 1, 0
    runLength = 0
    direction = 0

    while current < len(array):

        if array[current] > array[previous]:
            direction = 1
            runLength += 1
            previous, current = current, current + 1
        elif array[current] == array[previous]:
            runLength = 0
            previous, current = current, current + 1
            direction = 0
        else:
            if direction == 1:
                while current < len(array) and array[current] < array[previous]:
                    runLength += 1
                    previous, current = current, current + 1
                direction = 0
                if runLength > longestPeak:
                    longestPeak = runLength + 1
                    runLength = 0
            else:
                previous, current = current, current + 1
    
    return longestPeak

print(longestPeak([5, 4, 3, 2, 1, 2, 10, 12]))
            

        


        
