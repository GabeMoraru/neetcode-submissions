class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = []
        for word in strs:
            ret.append(str(len(word)))
            ret.append('-')
            ret.append(word)
        return "".join(ret)

    # 5-52345-78

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '-':
                j += 1
            leng = int(s[i:j])
            i = j + 1
            j = i + int(leng)
            res.append(s[i:j])
            i = j

        return res

                
