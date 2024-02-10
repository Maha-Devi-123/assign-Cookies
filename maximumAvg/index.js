/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findMaxAverage = function(nums, k) { 
    let cw_sum = nums.slice(0,k).reduce((ac,num) => ac+num,0) 
    let avg = cw_sum/k 
    for (let ind=k;ind<nums.length;ind++){
        const wsum=(cw_sum + nums[ind] - nums[ind-k])
        if((wsum / k )>avg){
            avg = (wsum / k )
        }
        cw_sum=wsum
    }
        return avg
    }; 