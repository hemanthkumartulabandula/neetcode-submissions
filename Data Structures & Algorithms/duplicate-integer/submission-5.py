class Solution:
    def hasDuplicate(self, nums: List[int]):
        a = {}

        for i in nums:
            if i not in a.keys():
                a[i] = 1
            else:
                a[i] += 1
        for i in a:
            if a[i] > 1:
                return True
        return False

        