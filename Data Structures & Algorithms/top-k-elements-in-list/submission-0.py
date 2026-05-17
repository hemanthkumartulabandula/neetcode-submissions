class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        first = []
        for it, cnt in freq.items():
            first.append([cnt, it])
        first.sort()

        final = []
        for i in range(k):
            final.append(first.pop()[1])
        return final
