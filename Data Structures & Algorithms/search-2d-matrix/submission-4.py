class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i,j=0,len(matrix)-1
        while i<=j:
            mid=(i+j)//2
            if matrix[mid][0]<=target<=matrix[mid][-1]:
                arr=matrix[mid]
                low,high=0,len(arr)-1
                while low<=high:
                    armid=(low+high)//2
                    if arr[armid]==target:
                        return True
                    elif arr[armid]<target:
                        low=armid+1
                    else:
                        high=armid-1
                return False
            elif matrix[mid][0]<target:
                i=mid+1
            else:
                j=mid-1
        return False