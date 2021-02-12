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
        output = ''
        i = 0
        while i < len(text):
            if text[i] == "&":
                end = text[i:].index(';')
                sub = text[i:end+i+1]
                print(sub, d.get(sub))
                if sub in d:
                    output += d[sub]
                    i = end+i+1
                else:
                    output += text[i]
                    i += 1
            else:
                output += text[i]
                i += 1
        return output
                
