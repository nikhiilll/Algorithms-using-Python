def popAndAdd(stack, result):

    count = 0
    while stack:
        popped_char = stack.pop()
        count += 1
    if count // 10 != 0:
        result.append('9')
        result.append(popped_char)
        result.append(str(count % 9)) 
        result.append(popped_char)
    else:
        result.append(str(count))
        result.append(popped_char)

def runLengthEncoding(string):

    stack = []
    result = []

    for c in string:

        if not stack or stack[-1] == c:
            stack.append(c)
        else:
            popAndAdd(stack, result)
            stack.append(c)
    
    popAndAdd(stack, result)
    return ''.join(result)

string = "AAAAAAAAAAAAABBCCCCDD"
print(runLengthEncoding(string))
