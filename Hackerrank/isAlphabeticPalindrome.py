# Complete the 'isAlphabeticPalindrome' function below.
#
# The function is expected to return a BOOLEAN.
# The function accepts STRING code as parameter.
"""Solution 1
loop through the string and construct a new string by adding each
alphabetic letter to the new string. Then check that the string is the same
forwards as backwards
Issue: Did not convert to lower"""
#

def isAlphabeticPalindrome(code):
    newStr = ""
    
    for char in code:
        if char.isalpha():
            newStr = char + newStr
    
    newStr = newStr.lower()
    
    if newStr == newStr[::-1] :
        return True
    return False
