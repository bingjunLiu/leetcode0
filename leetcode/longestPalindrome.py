class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_cover=s[::-1]
        i = 0
        str=""


        while ( i < len(s) ):
            str_tmp = ""
            while( s_cover[i]==s[i] ):
                str_tmp=str_tmp+s[i]
            if len(str) < len(str_tmp): str=str_tmp



