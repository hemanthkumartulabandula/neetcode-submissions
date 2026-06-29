class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numMap = {}
        for i in nums:
            if i not in numMap:
                numMap[i] = 1
            else:
                numMap[i] += 1
                return True
        return False