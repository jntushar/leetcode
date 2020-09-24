/*

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

*/



**********Solution***********


class Solution {
       private int find(int[] nums, int s, int e){
        int n = e-s+1;
        if(n == 1) return nums[s];
        if(n == 2) return Math.max(nums[s], nums[e]);
        int prev3 = nums[s], prev2 = nums[s+1], prev1 = Math.max(nums[s+2]+prev3, prev2);
        for(int i = s+3; i <= e; i++){
            int curr = nums[i] + Math.max(prev3, prev2);
            prev3 = prev2;
            prev2 = prev1;
            prev1 = curr;
        }
        return Math.max(prev1, prev2);
    }
    public int rob(int[] nums) {
        int n = nums.length;
        if(n == 0) return 0;
        if(n == 1) return nums[0];
        
        return Math.max(find(nums, 0, n-2), find(nums, 1, n-1));
    }
   
}