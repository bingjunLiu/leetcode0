class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        int2list = list(str(x))
        if int2list == int2list[::-1]:
            return True
        else:return False