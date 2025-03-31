class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else :
                r = m
        min_ind = l
        if min_ind == 0:
            l = 0
            r = n - 1
        elif nums[0]<= target <= nums[min_ind-1] :
            r = min_ind - 1
            l = 0
        else :
            r = n - 1
        while l <= r :
            m = (l+r)//2
            if nums[m] == target :
                return m
            elif target > nums[m] :
                l = m + 1
            else :
                r = m - 1
        return -1
