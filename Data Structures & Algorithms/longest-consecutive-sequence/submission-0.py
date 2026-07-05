class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if not nums:
            return 0
        count=1
        mcount=1
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                continue
            if nums[i-1]+1==nums[i]:
                count+=1
            else:
                count=1
            mcount=count if count>mcount else mcount
        return mcount


