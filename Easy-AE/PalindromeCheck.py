def isPalindrome(string):

    n = len(string)
    last_half = string[-1:n//2:-1]
    return(string[:n//2] == last_half)
    #return (string == string[::-1])

print(isPalindrome("abcdcba"))