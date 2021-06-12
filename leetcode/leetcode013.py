class Solution:
    def romanToInt(self, s: str) -> int:
        # dict_roma = dict()
        dict_roma = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans,i = 0,0
        while i < len(s):
            if i+1 < len(s) and dict_roma[s[i]] < dict_roma[s[i+1]]:
                ans += (dict_roma[s[i+1]] - dict_roma[s[i]] )
                i+=2
            else:
                ans +=dict_roma[s[i]]
                i+=1
        return ans