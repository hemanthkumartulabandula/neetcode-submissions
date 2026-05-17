class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        first = []
        for it, cnt in freq.items():
            first.append([cnt, it])
        first.sort()

        final = []
        for i in range(k):
            final.append(first.pop()[1])
        return final
