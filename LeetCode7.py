'''
LeetCode 7:

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.


Example:
    Input: x = 123
    Output: 321


This one stumped me TBH. Had to look up the mathematical process, so I kinda cheated.


Solved in Python


'''


x = -123

def reverseNumber(num):
    negative = False
    if num < 0:
        negative = True
        num = -num
    reversedNum = 0
    while num:
        reversedNum = reversedNum * 10 + num % 10
        num = num // 10
        
    if reversedNum <= -2 ** 31 or reversedNum >= 2 ** 31 - 1:
        return 0
    
    if negative:
        return -reversedNum
    else:
        return reversedNum





print(reverseNumber(x))



