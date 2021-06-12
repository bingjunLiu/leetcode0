import math
class Solution:
    def maxArea(self, height: List[int]) -> int:
        capacity=0
        max_heigh=0
        for i in range(len(height)-1):
            if max_heigh < height[i] : max_heigh=height[i]
            else:continue
            for j in range(i+1,len(height)):
                capacity_tmp=min(height[i], height[j]) * (j - i)
                if( capacity < capacity_tmp ): capacity = capacity_tmp
        return capacity

