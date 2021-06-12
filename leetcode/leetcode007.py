class Solution:
    def reverse(self, x: int) -> int:
        if_minus = 0
        if x < 0:
            x = str(x)
            x = list(x[1:])
            if_minus = 1
        else:
            x = list(str(x))
        ans=0
        for i in range(len(x)):
            ans += 10**(i)*int(x[i])
        if if_minus == 1:
            ans = -ans
        if ans < -2**31 or ans > 2**31-1:
            return 0
        return ans