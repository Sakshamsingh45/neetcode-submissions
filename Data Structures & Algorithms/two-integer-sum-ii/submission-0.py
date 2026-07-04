class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            left,right=i+1,len(numbers)-1
            while left<=right:
                mid=(left+right)//2
                s=numbers[mid]+numbers[i]
                if s==target:
                    return[i+1,mid+1]
                elif s<target:
                    left=mid+1
                else:
                    right=mid-1