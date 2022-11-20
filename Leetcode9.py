
'''
Leetcode question 9:

Given an integer x, return true if x is a palindrome, and false otherwise.

Solved in Python
'''
            

x = 123


def palindrome(num):
    spam = str(x)
    spam = list(spam)
    reversedSpam = []
    
    for i in range(len(spam),0,-1):
        reversedSpam.append(spam[i-1])           
    if spam == reversedSpam:
        return True
    else:
        return False
    
    
print(palindrome(x))  
