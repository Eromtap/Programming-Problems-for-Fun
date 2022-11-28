
'''

Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.


Honestly not sure why this is listed as "Hard" on Leetcode. This was by far the esiest challenge so far

'''

class Solution:
    def firstMissingPositive(self, nums):
        
        
        smallest = 0
        
        nums.sort()
        

        
        for i in nums:
            if i <= 0 or i == smallest:
                continue
            if smallest + 1 != i:
                return smallest + 1
            else:
                smallest = i
            
        
        return smallest + 1
        
        
        
        
numbers = [0,2,2,1,1]


x = Solution()
print(x.firstMissingPositive(numbers)  )           
