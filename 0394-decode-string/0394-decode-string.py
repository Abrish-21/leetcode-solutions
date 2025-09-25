class Solution:
    def decodeString(self, s: str) -> str:
        idx = 0
        def decode():
            nonlocal idx
            num = 0
            result = ""
            while idx < len(s):
                char = s[idx]
                if char.isdigit():
                    num = num * 10 + int(char)
                    # idx += 1
                elif char == '[':
                    idx += 1
                    create =  decode()
                    result += create * num
                    num = 0
                elif char == ']':
                    # idx += 1
                    return result
                else:
                    # idx += 1
                    result += char
                idx += 1
            return result
        return decode()

        