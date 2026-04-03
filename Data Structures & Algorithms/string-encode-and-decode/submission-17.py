class Solution:

    def encode(self, strs: List[str]) -> str:  
        encoded = ""      
        for s in strs:
            encoded += (str(len(s)) + "#" + s)
        
        return encoded
            


    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            size = ""
            # parse the length of the original word
            while s[i] != "#":
                size += s[i]
                i += 1
            if size.isdigit():
                i += 1 # skip delimiter
                decoded.append(s[i:i+int(size)])
                i += int(size)
        
        return decoded


