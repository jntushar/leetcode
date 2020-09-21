/*

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

*/


*********SOLUTION**********

class Solution {
    public String longestPalindrome(String s) {
        boolean[][] dp = new boolean[s.length()][s.length()];
        String res = "";
        int len = 0;
        for(int gap=0; gap<s.length(); gap++){
            for(int i=0, j=gap; j<s.length(); i++, j++){
                if(gap==0){
                    dp[i][j] = true;
                }else if(gap==1){
                    if(s.charAt(i) == s.charAt(j)){
                        dp[i][j] = true;
                    }else{
                        dp[i][j] = false;
                    }
                }else{
                    if(s.charAt(i) == s.charAt(j) && dp[i+1][j-1]){
                        dp[i][j] = true;
                    }else{
                        dp[i][j] = false;   
                    }
                }
                if(dp[i][j]){
                len=gap+1;
                }
            }  
        }
        
        for(int i=0,j=len-1; j<s.length(); j++,i++){
            String s1 = s.substring(i,j+1);
            StringBuilder s2 = new StringBuilder();
            s2.append(s1);
            s2 = s2.reverse();
            if(s1.equals(s2.toString())){
                res = s1;
                break;
            }
        }
        
        return res;
    }
}