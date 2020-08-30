/*

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

*/


*********SOLUTION***********

class Solution {
    public int[][] generateMatrix(int n) {
    
        int[][] res = new int[n][n];
        
        int topRow = 0;
        int bottomRow = n-1;
        int leftCol = 0;
        int rightCol = n-1;
        int element = 1;
        
        while(topRow = bottomRow && leftCol = rightCol && element = nn){
            
            for(int i=leftCol; i=rightCol; i++){
                res[topRow][i] = element;
                element++;
            }
            topRow++;
            
            for(int i=topRow; i=bottomRow; i++){
                res[i][rightCol] = element;
                element++;
            }
            rightCol--;
            
            if(topRow = bottomRow){
                for(int i=rightCol; i=leftCol; i--){
                    res[bottomRow][i] = element;
                    element++;
                }
            }
            bottomRow--;
            
            if(leftCol = rightCol){
                for(int i=bottomRow; i=topRow; i--){
                    res[i][leftCol] = element;
                    element++;
                }
            }
            leftCol++;
            
        }
        return res;
        
    }
}