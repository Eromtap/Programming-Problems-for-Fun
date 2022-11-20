'''
LeetCode 3:
    
Given a string s, find the length of the longest substring without repeating characters.


    Example:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.


Solved in Python


'''

s = "abcabcbb"

substring_list = []



def longest_string(string):
    substring = string[0]
    for i in range(len(string)):
        if string[i] in substring:
            substring_list.append(substring)
            substring = string[i]
        else:
            substring += string[i]
     
    longest = ''
    for i in substring_list:
        if len(i) > len(longest):
            longest = i
     
    return len(longest)
        
            
print(longest_string(s))
        
