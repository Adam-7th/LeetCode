class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_end_point=0
        for i in range(len(nums)):
            if max_end_point < i:
                return False
            max_end_point=max(max_end_point,i+nums[i])
        return True

            
