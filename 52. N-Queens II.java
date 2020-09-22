/*

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

*/


********Solution*********


class Solution {
	int ans=0;
	public int totalNQueens(int n) {
		if(n==0)
			return 0;
			
		nQueen_(n,0,0,new boolean[n],new boolean[2*n-1],new boolean[2*n-1]);
		return ans;
	}
	
   public void nQueen_(int n, int qpsf, int r, boolean[] col, boolean[] d1, boolean[] d2)      {
		if (qpsf == n) {
			ans++;
			return;
		}
		for (int c = 0; c < n; c++) {
			if (!col[c] && !d1[r + c] && !d2[n - 1 + r - c]) {
				col[c] = true;
				d1[r + c] = true;
				d2[n - 1 + r - c] = true;
				nQueen_(n , qpsf + 1, r + 1, col, d1, d2);
				col[c] = false;
				d1[r + c] = false;
				d2[n - 1 + r - c] = false;
			}
		}
	}
}