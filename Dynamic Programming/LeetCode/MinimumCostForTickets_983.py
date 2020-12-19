def minimumCostForTickets(days, costs):

    costArray = [0 for i in range(days[-1] + 1)]

    for i in range(1, days[-1] + 1):

        if i not in days:
            costArray[i] = costArray[i - 1]
        else:
            costArray[i] = min(costArray[max(0, i - 1)] + costs[0], costArray[max(0, i - 7)] + costs[1], costArray[max(0, i - 30)] + costs[2])
        
    return costArray[-1]

print(minimumCostForTickets([1,4,6,7,8,20], [2,7,15]))