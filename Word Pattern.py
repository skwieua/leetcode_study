class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dicPtn = {}
        ptns = [i for i in pattern]
        string_s = s.split()

        if len(ptns) != len(string_s):
            return False

        for ptn in zip(ptns, string_s):
            if ptn[0] not in dicPtn:
                if ptn[1] in dicPtn.values():
                    return False
                else:
                    dicPtn[ptn[0]] = ptn[1]
            else:
                if dicPtn[ptn[0]] != ptn[1]:
                    return False

        return True


pattern = "abba"
# s = "dog cat cat dog"
s = "dog cat cat fish"
# s = "dog dog dog dog"

a = Solution()
print(a.wordPattern(pattern, s))