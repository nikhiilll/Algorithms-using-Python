class MinMaxStack:

    def __init__(self):
        self.stack = []
        self.minmaxStack = []

    def peek(self):
        return self.stack[-1]

    def pop(self):
        self.minmaxStack.pop()
        return self.stack.pop() 

    def push(self, number):
        
        newMinMax = {"min": number, "max": number}
        if self.minmaxStack:
            currentMinMax = self.minmaxStack[-1]
            newMinMax["min"] = min(newMinMax["min"], currentMinMax["min"])
            newMinMax["max"] = max(newMinMax["max"], currentMinMax["max"])
        self.minmaxStack.append(newMinMax)
        self.stack.append(number)

    def getMin(self):
        
        return self.minmaxStack[-1]["min"]

    def getMax(self):
        
        return self.minmaxStack[-1]["max"]
