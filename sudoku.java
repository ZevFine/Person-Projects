

 import java.io.*;   // allows us to read from a file
 import java.util.*;
 
 public class sudoku {    
     
     private int[][] grid;
     
     
     private boolean[][] valIsFixed;
     
     
     private boolean[][][] subgridHasVal;
     
     private boolean[][] hasIncol;
     private boolean[][] hasinRow;
     
    
     public sudoku() {
         this.grid = new int[9][9];
         this.valIsFixed = new boolean[9][9];     
         this.subgridHasVal = new boolean[3][3][10];        
         this.hasIncol = new boolean[9][10];
         this.hasinRow = new boolean[9][10];
     }
     
 
     public void placeVal(int val, int row, int col) {
        //places val in row,col and updates and necessary array 
         this.grid[row][col] = val;
         this.subgridHasVal[row/3][col/3][val] = true;
         this.hasIncol[col][val] = true;
         this.hasinRow[row][val] = true;
 
 
     }
         
     public void removeVal(int val, int row, int col) {
        //remoces val in row,col and updates and necessary array 
         this.grid[row][col] = 0;
         this.subgridHasVal[row/3][col/3][val] = false;
        this.hasIncol[col][val] = false;
         this.hasinRow[row][val] = false;
 
     }  
         
  
     public void readConfig(Scanner input) {
        //reads the txt files to solve the sudoku
         for (int r = 0; r < 9; r++) {
             for (int c = 0; c < 9; c++) {
                 int val = input.nextInt();
                 this.placeVal(val, r, c);
                 if (val != 0) {
                     this.valIsFixed[r][c] = true;
                     this.subgridHasVal[r/3][c/3][val] = true;
                     this.hasIncol[c][val] = true;
                     this.hasinRow[r][val] = true;
                                 }
             }
         }

     }
                 
             
     public void printGrid() {
         for (int r = 0; r < 9; r++) {
             this.printRowSeparator();
             for (int c = 0; c < 9; c++) {
                 System.out.print("|");
                 if (this.grid[r][c] == 0) {
                     System.out.print("   ");
                 } else {
                     System.out.print(" " + this.grid[r][c] + " ");
                 }
             }
             System.out.println("|");
         }
         this.printRowSeparator();
     }
         
   
     private static void printRowSeparator() {
         for (int i = 0; i < 9; i++) {
             System.out.print("----");
         }
         System.out.println("-");
     }
     
     
     private boolean solveRB(int n) {
        //recursive backtracking method that actually solves the sudoku
         if(n == 81){
             return true;
         }
         int r = n/9;
         int c = n - r * 9;
         if(valIsFixed[r][c] == true){
             if(solveRB(n+1)){
                 return true;
                 }
             }
             else{
             for(int i = 1; i < 10; i++){
                 if(subgridHasVal[r/3][c/3][i] == false &&
                 hasIncol[c][i] == false &&
                 hasinRow[r][i] == false){
                     placeVal(i, r, c);
                      if(solveRB(n+1)){
                     return true;
                 } 
                 this.removeVal(i, r, c);
             }
             }   
         }             
         
        
      return false;
     } 
 
     
     
     public boolean solve() { 
         boolean foundSol = this.solveRB(0);
         return foundSol;
     }
     
     public static void main(String[] args) {
         Scanner scan = new Scanner(System.in);
         sudoku puzzle = new sudoku();
         
         System.out.print("Enter the name of the puzzle file: ");
         String filename = scan.nextLine();
         System.out.println(filename);
         
         try {
             Scanner input = new Scanner(new File(filename));
             puzzle.readConfig(input);
             input.close();
         } catch (IOException e) {
             System.out.println("error accessing file " + filename);
             System.out.println(e);
             System.exit(1);
         }
         
         System.out.println();
         System.out.println("Here is the initial puzzle: ");
         puzzle.printGrid();
         System.out.println();
         
         if (puzzle.solve()) {
            System.out.println("Here is the solution: ");
         } else {
            System.out.println("No solution could be found.");
            System.out.println("Here is the current state of the puzzle:");
         }
         puzzle.printGrid();  
         scan.close();
         
     }    
 }
 