1class Solution:
2    def isPalindrome(self, s):
3        left, right = 0, len(s) - 1
4        
5        while left < right:
6            # move left to next valid char
7            while left < right and not s[left].isalnum():
8                left += 1
9            
10            # move right to previous valid char
11            while left < right and not s[right].isalnum():
12                right -= 1
13            
14            # compare (case-insensitive)
15            if s[left].lower() != s[right].lower():
16                return False
17            
18            left += 1
19            right -= 1
20        
21        return True
22        