class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = "".join(x for x in s if x.isalnum())
        lower = cleaned_str.lower()
        return lower == lower[::-1]