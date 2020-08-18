def funnyString(s):

    rev = s[::-1]
    for i in range(len(s)-1):
        if abs(ord(s[i+1]) - ord(s[i])) != abs(ord(rev[i+1]) - ord(rev[i])):
            return "Not Funny"
    return "Funny"
