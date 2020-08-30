/*

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

*/


******SOLUTION*******


class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        
        List<Integer> res = new ArrayList<>();
        
        if(matrix.length == 0)
            return res;
        
        int topRow = 0;
        int bottomRow = matrix.length - 1;
        int leftCol = 0;
        int rightCol = matrix[0].length - 1;
        
        while(topRow <= bottomRow && leftCol <= rightCol){
            
            for(int i=leftCol; i<=rightCol; i++){
                res.add(matrix[topRow][i]);   
            }
            topRow++;
            
            for(int i=topRow; i<=bottomRow; i++){
                res.add(matrix[i][rightCol]);
            }
            rightCol--;
            
            
            if(topRow <= bottomRow){
                for(int i=rightCol; i>=leftCol; i--){
                    res.add(matrix[bottomRow][i]);
                }
            }
            bottomRow--;
            
            if(leftCol <= rightCol){
                for(int i=bottomRow; i>=topRow; i--){
                    res.add(matrix[i][leftCol]);
                }
            }
            leftCol++;
            
            
        }
        
        return res;
    }
}