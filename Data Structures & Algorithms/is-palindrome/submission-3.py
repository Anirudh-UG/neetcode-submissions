class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # O(n) and O(n) space and time complexity 
        # cleaned_str = "".join(x for x in s if x.isalnum())
        # lower = cleaned_str.lower()
        # return lower == lower[::-1]
        ptr_1, ptr_2 = 0, len(s) -1

        while ptr_1 < ptr_2:

            # If not alnum, skip to the next index    
            while ptr_1 < ptr_2 and not s[ptr_1].isalnum():
                ptr_1 += 1

            # If not alnum, skip to the next index
            while ptr_1 < ptr_2 and not s[ptr_2].isalnum():
                ptr_2 -= 1
            
            if s[ptr_1].lower() != s[ptr_2].lower():
                return False
            ptr_1, ptr_2 = ptr_1 + 1, ptr_2 - 1
        return True
            