def powerset(array):
    
    results = [[]]
    powersetHelper(array, [], results)
    return results

def powersetHelper(array, currentCombination, results):

    if len(array) == 0:
        return
    
    for i in range(len(array)):
        newCurrentCombination = currentCombination
        newCurrentCombination.append(array[i])
        results.append(newCurrentCombination)
        powersetHelper(array[i:], newCurrentCombination, results)
    
print(powerset([1, 2, 3]))

