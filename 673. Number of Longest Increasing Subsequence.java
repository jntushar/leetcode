/*

Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.

*/


************SOLUTION************


class Solution {
    
    public class Pair{
        int index;
        int length;
        int value;
        
        Pair(int index, int length, int value){
            this.index = index;
            this.length = length;
            this.value = value;
        }
    }
    
    public int findNumberOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        int omax = 0;
        int res = 0;
        
        for(int i=0; i<nums.length; i++){
            int max = 0;
            for(int j=0; j<i; j++){
                if(nums[j] < nums[i]){
                    if(dp[j] > max){
                        max = dp[j];
                    }
                }
            }
            dp[i] = max + 1;
            if(dp[i] > omax){
                omax = dp[i];
            }
        }
        
        ArrayDeque<Pair> queue = new ArrayDeque<>();
        
        for(int i=0; i<dp.length; i++){
            if(dp[i] == omax){
                queue.add(new Pair(i, omax, nums[i]));
            }
        }
        
        while(queue.size() > 0){
            Pair rem = queue.removeFirst();
            if(rem.length == 1){
                res++;
            }
            for(int j=0; j<rem.index; j++){
                if(nums[j] < rem.value){
                    if(dp[j] == rem.length - 1){
                        queue.add(new Pair(j, dp[j] , nums[j]));
                    }
                }
            }
        }
        
        return res;
    }
}
