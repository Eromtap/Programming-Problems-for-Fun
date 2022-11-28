'''
LeetCode 3:
    
Given a string s, find the length of the longest substring without repeating characters.


    Example:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.


Solved in Python


'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):

        longest = 0
        
        # If len(s) is 1, the answer is 1
        if len(s) == 1:
            return 1
        # If s is empty string, return 0
        if not s:
            return 0


        # Two pointer approach. i is slow pointer, j is fast pointer
        for i in range(len(s)):

            for j in range(i+1, len(s)):
                # if no repeats found after 95 characters
                # return 95 (since that's as long as it can be without repeats)
                if j-i == 95:
                    return 95
                # Check if fast pointer value is in the substring.
                # If it is, check if fast pointer index - slow pointer index
                # is greater than longest substring. If it is, longest = difference
                if s[j] in s[i:j]:
                    
                    if j-i > longest:
                        longest = j-i

                    break
                # Last check if the last substring ending on 
                # the last character is longer than 'longest'
                if j == len(s)-1:
                    if j-i+1 > longest:
                        longest = j-i+1
    
        return longest    
        
