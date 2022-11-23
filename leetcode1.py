'''
Leetcode question 1:

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Solved in Python cause I don't know Jave (yet).

'''






nums = [2,7,11,15]
target = 9

class Solution(object):
    def twoSum(self, nums, target):
        outputList = []
        
        pos_count = 0
        neg_count = 0
        
        for i in nums:
            if i >= 0:
                pos_count += 1
        if pos_count == len(nums) and target < 0:
            return []
       
        for i in nums:
            if i < 0:
                neg_count += 1
        if neg_count == len(nums) and target >= 0:
            return []            

        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    outputList.append(i)
                    outputList.append(j)
                    return outputList
            
