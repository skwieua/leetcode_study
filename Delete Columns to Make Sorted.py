class Solution:
    def minDeletionSize(self, strs: list[str]) -> int:
        cnt = 0
        length = len(strs)
        a = "".join(strs)
        length1 = len(a) // length
        for i in range(length1):
            value = (a[i::length1])
            if value != "".join(sorted(value)):
                cnt += 1

        return cnt

a = Solution()
a.minDeletionSize(["cba","daf","ghi"])