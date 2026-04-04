class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for a in range(len(nums)):
            for b in range(a+1, len(nums)):
                if nums[a] == nums[b]:
                    return True
        return False
