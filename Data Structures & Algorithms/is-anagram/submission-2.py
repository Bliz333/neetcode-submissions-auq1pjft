class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # 2) 统计 s 每个字符出现次数
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        # 3) 用 t 抵消次数
        for c in t:
            if c not in count or count[c] == 0:
                return False
            count[c] -= 1

        return True

