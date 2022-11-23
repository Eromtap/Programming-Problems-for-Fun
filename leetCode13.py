
'''
Leetcode question 13:

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, 
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. The same principle applies to the number nine, 
which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

Solved in Python    
'''
            

s = "LVIII"


class Solution(object):
    def romanToInt(self, numeral):
        
        x = 0

        for i in range(len(numeral)):

            if i == len(numeral)-1:
                if numeral[i] == 'I':
 
                    x += 1
                elif numeral[i] == 'V':

                    x += 5
                elif numeral[i] == 'X':
 
                    x += 10
                elif numeral[i] == 'L':
                    x += 50
                elif numeral[i] == 'C':
                    x += 100
                elif numeral[i] == 'D': 
                    x += 500
                elif numeral[i] == 'M': 
                    x += 1000

                return x               

            if numeral[i] == 'I':
                if numeral[i+1] == 'V' or numeral[i+1] == 'X':
                    x -= 1
                else:
                    x += 1

            if numeral[i] == 'V':
                x += 5

            if numeral[i] == 'X':
                if numeral[i+1] == 'L' or numeral[i+1] == 'C':
                    x -= 10
                else:
                    x += 10

            if numeral[i] == 'L':
                x +=  50

            if numeral[i] == 'C':
                if numeral[i+1] == 'D' or numeral[i+1] == 'M':
                    x -= 100
                else:
                    x += 100

            if numeral[i] == 'D':
                x += 500

            if numeral[i] == 'M':
                x += 1000
