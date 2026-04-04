class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
            # 2) dp[i] 表示：以 nums[i] 结尾的最长递增子序列长度
        n = len(nums)
        dp = [1] * n   # 每个位置至少为 1（自己单独成一队）

        # 3) 从左到右，依次计算每个 dp[i]
        for i in range(1, n):
            # 4) 往左看所有 j < i
            for j in range(0, i):
                # 5) 如果 nums[j] < nums[i]，就能把 i 接在 j 后面
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        # 6) 整个 dp 的最大值就是答案
        return max(dp)