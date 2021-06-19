class Solution:
    def intToRoman(self, num: int) -> str:
        dict_roma = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        dict_int ={ dict_roma[i]: i for i in dict_roma.keys()}
        list_sp = [1,10,100]
        # int2list = list(str(num))
        ans = ''
        for i in dict_int.keys()[::-1]:
            if list(str(num))[0] == '9' or list(str(num))[0] == '4' and  i != 1000:
                for j in list_sp[::-1]:
                    tmp_49 = int(num / j)
                    if tmp_49 == 4 :
                        ans += dict_int[j] + dict_int[list(dict_int.keys()).index(j) + 1]
                    elif tmp_49 == 9:
                        ans += dict_int[j] + dict_int[list(dict_int.keys()).index(j) + 2]
                    num -= tmp_49 * j
            else:
                count = int(num / i)
                ans += dict_int[i] * count
                num -= count*i
        return ans

if __name__ =="__main__":
    print()

