class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [0] * len(nums)
        l_mult = 1
        r_mult = 1
        for i in range(len(nums)) :
            out[i] = l_mult
            l_mult *= nums[i]
        for j in range(len(nums)-1,-1,-1) :
            out[j] *= r_mult
            r_mult *= nums[j]
        return out
        