package LEARNING.JavaTutorial;

public class javaForLoops {
    static int num = 3;
    public static void main(String[] args) {
        /* 
        for (statement 1; statement 2; statement 3) {
            // code block to be executed
        }
        Statement 1 is executed (one time) before the execution of the code block.

        Statement 2 defines the condition for executing the code block.

        Statement 3 is executed (every time) after the code block has been executed.
        */
        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 3; j++) {
                System.out.print(i * j + " ");
            }
            System.out.println();
        }
        /*
        FOR-EACH (kind of like a python for loop)
        for (type variableName : arrayName) {
            code block to be excecuted
        }
        */

        int[] y = {2,3,4,5,6};
        for (int number:y){
            System.out.println(number);
        }
    }   
}
