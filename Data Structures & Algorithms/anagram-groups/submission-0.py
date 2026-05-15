class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        final = []
        visited = set()

        for a in range(len(strs)):
            if a in visited:
                continue
            sub = []
            sub.append(strs[a])
            for b in range(a+1, len(strs)):
                
                if sorted(strs[a]) == sorted(strs[b]):
                    
                    sub.append(strs[b])
                    visited.add(b)
                    
            final.append(sub)
        return final
                    


        