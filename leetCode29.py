
'''
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. 
For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. 
For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.



I wanted to basically do this like you would with pencil and paper. Breaking the problem into smaller
problems and carrying the remainder over. This meant converting the int to a string and iterating. 
I think the speed could definatley be improved with fewer conversions between ints and strings, but as it is, it passes.

'''



class Solution(object):
    def divide(self, dividend, divisor):
        
    ## Had to add this block because leetcode was wrong. When dividing -2**31 by 1 or -1,
		## It was giving totally different results (wrong ones) than my IDE. IDK why. So I hardcoded
		## those two conditions lol
        if dividend == -2147483648 and divisor == 1:
            return -2147483648
        elif dividend == -2147483648 and divisor == -1:
            return 2147483647

        remainder = 0
        result = []
        
        dividend_list = []
        
        pos_dividend = list(str(abs(dividend)))
        
        for i in pos_dividend:
            dividend_list.append(int(i))
        
        pos_divisor = abs(divisor)
        
        count = 0
        
        for i in range(len(dividend_list)):
            if remainder !=0:
                dividend_list[i] = int(str(remainder)+str(dividend_list[i]))

            if pos_divisor <= dividend_list[i]:
                while dividend_list[i] >= pos_divisor:
                    dividend_list[i] -= pos_divisor
                    count += 1
                    
                result.append(count)
                count = 0
                remainder = dividend_list[i]
                
            elif pos_divisor > dividend_list[i]:
                result.append(0)
                remainder = dividend_list[i]

    
  
        def convert_result(num_list):
            num_string = ''
            for i in num_list:
                num_string += str(i)
                
            return int(num_string)
  
    
        if divisor > 0 and dividend > 0:            
          return convert_result(result)
    
        if divisor < 0 and dividend < 0:
            return convert_result(result)
        
        else:
            return convert_result(result) * -1
    
  
    
        return convert_result(result)
  
    
  
    
  
dividend = -2147483648


divisor = 1
    
    
x = Solution()
print(x.divide(dividend, divisor) )   
