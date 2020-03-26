"""

Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

"""

"""---SOLUTION---"""

class Solution:
    def decodeString(self, s):
        stack_strs = []  
        stack_nums = []  
        num = ""  
        str_t = ""  
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch == "[":
                stack_strs.append(str_t)
                stack_nums.append(int(num))
                num, str_t = "", ""  
            elif ch == "]":
                n = stack_nums.pop()  
                t = stack_strs.pop()  
                str_t = t + str_t * n
            else:  
                str_t += ch
        return str_t