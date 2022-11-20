'''
LeetCode 6:
    
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"


Solved in Python


'''


s = "PAYPALISHIRING"


def zigZag(string, numRows):
    
    end_string = ""
    step = 2 * numRows - 2
    
    if s == None:
        return ""
    if numRows == 1:
        return s
    
    for i in range(0, numRows):
        for j in range(i, len(s), step):
            end_string += s[j]
            if i != 0 and i != numRows - 1 and (j + step - 2 * i) < len(s):
                end_string += s[j + step - 2 * i]
    return end_string    


    
print(zigZag(s, 3))

























