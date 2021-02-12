class Solution:
    def entityParser(self, text: str) -> str:
        d = {
            "&quot;": '"',
            "&apos;": "'",
            "&amp;": "&",
            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/"
        }
        tmp = "!@#$%"
        for k, v in d.items():
            text = text.replace(k, v+tmp)
        return text.replace(tmp, '')
                
