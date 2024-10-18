def scoreOfString(s):
    if not s:  # Handle empty string case
        return 0
    
    res = 0
    for i in range(len(s) - 1):
        res += abs(ord(s[i]) - ord(s[i + 1]))
    return res

# Example usage
s = "abc"
print("Score of the string:", scoreOfString(s))  # Output: 2
