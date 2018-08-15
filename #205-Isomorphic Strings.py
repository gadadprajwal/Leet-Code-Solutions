class Solution(object):
    def isIsomorphic(self, s, t):
        
        
        # Comparing the len of unique elements in the string with the length of the unique combinations with each element in s with element in t in a sequence which is the requirement of the question to replace the elements in s by elements in t.
        return len(set(zip(s,t))) == len(set(s)) == len(set(t))
        
#         print(len(set(zip(s,t))))
#         if ls != lt:
#             return False
#         else:
#             for char in s:
#                 if char in dict_s:
#                     dict_s[char] += 1
#                 else:
#                     dict_s[char] = 1

#             for char in t:
#                 if char in dict_t:
#                     dict_t[char] += 1
#                 else:
#                     dict_t[char] = 1
        
        
#         print(dict_s,dict_t)
        
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
