class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) < 1:
            return "None"


        return "<ThisisabreakIwillani>".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        
        return s.split("<ThisisabreakIwillani>")