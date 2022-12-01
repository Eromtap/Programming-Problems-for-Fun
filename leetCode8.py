
'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

    Read in and ignore any leading whitespace.
    Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. 
    This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
    Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
    Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. 
    Change the sign as necessary (from step 2).
    If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
    Return the integer as the final result.



Honestly my least favorite challenge to date. It wasnt difficult persay, just tedious. 
I'd get a script and it would fail for wrong answers over and over for conditions I hadn't thought of...
So I had to add a condition for each one. Over and over and over..... GRRRR. Anyway, works now.
'''




class Solution:
    def myAtoi(self, s: str) -> int:
        try:
            if s == "":
                return 0
            if len(s) == 1 and not s.isdecimal():
                return 0
            
            cleaned_s = ""
            isNeg = False
            
            for i in range(len(s)):
                
                if cleaned_s == "" and s[i] == ' ':
                    continue
                if cleaned_s != "" and s[i] == ' ':
                    break
                if cleaned_s == "" and s[i] == '0':
                    if s[i+1].isdecimal():
                        continue
                    else:
                        return 0
                if cleaned_s == "" and s[i] == '-':
                    if s[i+1].isdecimal():
                        isNeg = True
                    else:
                        return 0
                if cleaned_s == "" and s[i] == '+':
                    if s[i+1].isdecimal():
                        continue
                    else:
                        return 0
                if cleaned_s != "" and s[i] == '+':
                    break
                if cleaned_s == "" and s[i].isalpha():
                    return 0
                if cleaned_s != "" and s[i].isalpha():
                    break
                if s[i] == '.':
                    break
                elif s[i].isdecimal():
                    cleaned_s += s[i]

            int_s = int(cleaned_s)
            
            if isNeg:
                int_s = int_s*-1
            
            if int_s <= -2**31:
                return -2147483648
            elif int_s >= 2**31 - 1:
                return 2147483647
            
            else:

                return int_s
        except:
            return 0
 
