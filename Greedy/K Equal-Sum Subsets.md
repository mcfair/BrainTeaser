```Java
class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        //only one partition
        if (k ==1 ) return true;
        
        //more partition than number of elements
        int n = nums.length;
        if ( k > n) return false;
        
        //total sum can't be divided by k
        int sum = 0; 
        for (int x: nums) sum += x;  
        if (sum % k != 0) return false;   
        
        Arrays.sort(nums);
        int target = sum/k;
        
        int[] v = new int[k];
        return helper(nums, target, v, n - 1);
        
    }
    
    


    public boolean helper(int[] nums, int target, int[] v, int idx) {
        // if all numbers are traversed
        if (idx < 0) {
            for (int t : v) {
                if (t != target) return false;
            }
            return true;
        }
        
        //try to fit the current number into each subset
        int num = nums[idx];
        for (int i = 0; i < v.length; ++i) {
            
            //if num is too big to fit in, try next subset
            if (v[i] + num > target) 
                continue; 
            //else do recursion
            else{
                v[i] += num;
                if (helper(nums, target, v, idx - 1)) 
                    return true;
                else 
                    v[i] -= num;
            }

        }
        return false;
    }
}
```
