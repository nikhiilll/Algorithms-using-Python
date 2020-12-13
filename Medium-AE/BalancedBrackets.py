def balancedBrackets(string):
    
    openingBrackets = "{[("
    closingBrackets = "}])"
    matchingBrackets = {"}" : "{", ")" : "(", "]" : "["}

    stack = []

    for character in string:
        if character in openingBrackets:
            stack.append(character)
        elif character in closingBrackets:
            if stack and stack[-1] == matchingBrackets[character]:
                stack.pop()
            else:
                return False
        else:
            continue
    
    return len(stack) == 0

print(balancedBrackets("([])(){}(())()()"))
