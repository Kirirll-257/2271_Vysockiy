public class Main{
    public static void main(String[] args){
        int[][] m = {{1, 2, 3}, {4, 0, 6}, {7, 8, 9}};
        outer:
        for (int i = 0; i < m.length; i++) {
            for (int j = 0; j < m[i].length; j++) {
                if (m[i][j] == 0) {
                   System.out.println("Found " + i + " and " + j);
                   break outer;  
                }
            }
        }
    }
}