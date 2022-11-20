'''
Leetcode question 1:

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Solved in Python cause I don't know Jave (yet).

'''






nums = [2,7,11,15]
target = 9



def adding(numList, result):
    outputList = []

    for i in nums:
        for j in range(len(nums)-1):
            if i + nums[j+1] == target:
                outputList.append(nums.index(i))
                outputList.append(j+1)
                return outputList

            
       
print(adding(nums, target))   
            
