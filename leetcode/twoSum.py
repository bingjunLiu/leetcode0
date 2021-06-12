class Solution:
    def twoSum(self,nums,target) :
        """
        :param nums: List[int]
        :param target: int
        :return: List[int]
        """
        hashmap={}
        for index,num in enumerate(nums):
            if num in hashmap:
                return [hashmap[num],index]
            hashmap[target-num]=index
        return None


