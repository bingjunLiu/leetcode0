class Solution:
    def convert(self, s: str, numRows: int):
        total=[]
        flag=0
        if numRows ==1:
            return s
        while flag < len(s):
            a = [' '] * numRows
            if len(total) % (numRows-1 ) ==0:

                for i in range(numRows):
                    if flag < len(s):
                        a[i]=s[flag]
                        flag+=1
                    else:break
                total.append(a)
            else:
                if flag < len(s):
                    row=len(total) % (numRows-1) +1
                    a[numRows-row]=s[flag]
                    flag+=1
                    total.append(a)
                else:break
        # step 2
        str=''
        for i in range(numRows):
            for maid in total:
                if maid[i]==' ':continue
                str=str+maid[i]
        return str

a=Solution()
total=a.convert(s="PAYPALISHIRING",numRows=3)
print(total)

