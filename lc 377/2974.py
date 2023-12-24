class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr=[]
        nums.sort()
        for i in range(0,len(nums),2):
            a,b=nums[i],nums[i+1]
            arr.append(b)
            arr.append(a)
        
        return arr