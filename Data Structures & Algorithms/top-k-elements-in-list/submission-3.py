class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for n in nums:
            freq[n] = 1 + freq.get(n, 0)

        first = []

        for it, cnt in freq.items():
            first.append([cnt, it])
        first.sort()
        final = []
        for _ in range(k):
            final.append(first.pop()[1])
        return final