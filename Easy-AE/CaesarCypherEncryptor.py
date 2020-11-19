def caesarCipherEncryptor(string, key):
    
    char_dict = {}
    new_string = []
    for i in range(26):
        char_dict[chr(97 + i)] = i
    
    for c in string:
        new_char = (char_dict[c] + key) % 26
        new_string.append(chr(new_char + 97))
    
    return ''.join(new_string)

"""
TC: O(n), SC: O(n)
"""
print(caesarCipherEncryptor("xyz", 2))
