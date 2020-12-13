def longestPalindromicSubstring(string):
    
    palindromeString = ""

    for palindromeLength in range(0, len(string)):
        i = 0
        while i + palindromeLength < len(string):

            tempString = string[i: i + palindromeLength + 1]
            if tempString == tempString[::-1]:
                if len(tempString) > len(palindromeString):
                	palindromeString = tempString
            i += 1
    
    return palindromeString