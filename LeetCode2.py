'''
LeetCode 2:

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.    
    
    Example:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.    
    
Solved in Python
OK, I kind of cheesed this one. just reversed the list, converted to strings,
then converted to int. Then did the math, and in the final return statement,
converted back to str, then list. Probably a stupid way to do it, but whatever lol


'''



l1 = [2,4,3]
l2 = [5,6,4]


def add_lists(l1, l2):
    
    l1_formatted = ''
    l2_formatted = ''
    final_list = []
    
    l1.reverse()
    l2.reverse()
    
    for i in l1:
        l1_formatted += str(i)
    l1_formatted = int(l1_formatted)
    
    for i in l2:
        l2_formatted += str(i)
    l2_formatted = int(l2_formatted)
    
    
    output = list(str(l1_formatted + l2_formatted))
    output.reverse()
    
    return output

    
    
    
    
    
print(add_lists(l1, l2))  
