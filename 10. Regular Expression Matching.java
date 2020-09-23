/*

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

*/



*********SOLUTION**********


class Solution {
    public boolean isMatch(String s, String p) {
        boolean[][] dp = new boolean[p.length() + 1][s.length() + 1];
		
		for(int i=0; i<dp.length; i++) {  // i is for pattern
			for(int j=0; j<dp[0].length; j++) {    // j is for string
				if(i==0 && j==0) {
					dp[i][j] = true;
				}else if(i==0) {        // First Row
					dp[i][j] = false;
				}else if(j==0) {        // First Column
					char pc = p.charAt(i-1);
					if(pc == '*') {
						dp[i][j] = dp[i-2][j];
					}else {
						dp[i][j] = false;
					}
				}else {
					char pc = p.charAt(i-1);   // pattern character
					char sc = s.charAt(j-1);   // string character
					if(pc == '*') {
						dp[i][j] = dp[i-2][j];
						char pslc = p.charAt(i-2);    //pattern second last character
						if(pslc == sc || pslc =='.'){
							dp[i][j] = dp[i][j] || dp[i][j-1];
						}
					}else if(pc == '.') {
						dp[i][j] = dp[i-1][j-1];
					}else if(pc == sc) {
						dp[i][j] = dp[i-1][j-1];
					} else {
						dp[i][j] = false;
					}
				}
			}
		}
		
		return dp[p.length()][s.length()];
    }
}