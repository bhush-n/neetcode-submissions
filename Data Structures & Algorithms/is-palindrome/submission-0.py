class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = ""

        for i in s:
            if i.isalnum():
                rev += i.lower()

        return rev == rev[::-1]