class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower().split(" ")
        s = "".join(s)
        s = [char for char in s if char.isalnum()]
        s = "".join(s)
        length = len(s)

        Half1 = sorted(s[0:((length - 1) // 2) + 1])
        Half2 = sorted(s[length // 2:length])

        if Half1 == Half2:
            return True
        else:
            return False