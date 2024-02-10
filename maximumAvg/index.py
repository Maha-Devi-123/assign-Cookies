class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total_sum=sum(nums[:k])
        avg= total_sum/k
        for ind in range(k,len(nums)):
            cavg=(total_sum + nums[ind]-nums[ind-k] )/k 
            if cavg > avg :
                avg=cavg 
            total_sum = total_sum + nums[ind]-nums[ind-k]
        return avg