class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for st in strs:
            encoded += str(len(st)) + "#" + st
        return encoded 

    def decode(self, s: str) -> List[str]:
        dec = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j = j + 1
            
            num = int(s[i:j])
            dec.append(s[j+1 : j+1+num])
            i = j + 1+ num
        
        return dec
