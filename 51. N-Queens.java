/*

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example

Input 4
Output [
 [.Q..,   Solution 1
  ...Q,
  Q...,
  ..Q.],

 [..Q.,   Solution 2
  Q...,
  ...Q,
  .Q..]
]
Explanation There exist two distinct solutions to the 4-queens puzzle as shown above.

*/


******Solution********



class Solution {
    public List<List<String>> solveNQueens(int n) {
        List<List<String>> result = new ArrayList<>();
        int[] arr = new int[n];
        helper(arr, 0, result);
        return result;
    }
	/** backtracking helper function, index is the current row where we are going to put the queue */
    private void helper(int[] arr, int index, List<List<String>> result) {
        if (index >= arr.length) {
            result.add(convert(arr));
            return;
        }
        for (int i = 0; i < arr.length; i++) {
            if (isValid(arr, index, i)) {
                arr[index] = i;
                index++;
                helper(arr, index, result);
                index--;
                arr[index] = 0;
            }
        }
    }
	/** the helper function check whether next position is valid */
    private boolean isValid(int[] arr, int index, int value) {
        for (int i = 0; i < index; i++) {
            if (arr[i] == value) return false;
            if (index + value == i + arr[i]) return false;
            if (index - value == i - arr[i]) return false;
        }
        return true;
    }
	/** convert the array to the string result */
    private List<String> convert(int[] arr) {
        List<String> result = new ArrayList<>();
        for (int i = 0; i < arr.length; i++) {
            StringBuilder curr = new StringBuilder();
            for (int j = 0; j < arr.length; j++) {
                curr.append(arr[i] == j ? 'Q' : '.');
            }
            result.add(curr.toString());
        }
        return result;
    }
}