class Solution:
    def countAndSay(self, n: int) -> str:
        tmp = ['1']
        if n == 1:
            return tmp[-1]
        else:
            for i in range(n-1):
                tmp.append(self.get_str(tmp[-1]))
            return tmp[-1]

    def get_str(self,str0:str):
        tmp_factor = str0[0]
        result_str = ''
        count = 1
        for i in list(str0)[1:]:
            if i == tmp_factor:
                count += 1
            if i != tmp_factor:
                result_str += str(count)+tmp_factor
                tmp_factor = i
                count = 1
        result_str += str(count) + tmp_factor
        return result_str

test_function = Solution()
print(test_function.get_str('1112'))










