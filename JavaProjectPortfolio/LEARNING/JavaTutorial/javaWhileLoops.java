package LEARNING.JavaTutorial;

public class javaWhileLoops {
    public static void main(String[] args) {
        /*
        WHILE LOOP:

        while (condition) {
            code block to be executed
        }        
        */

        /*
        DO/WHILE LOOP (Executes once whether the condition is true or false)

        do {
            code block to be executed
        } while (condition);
        */

        int i = 10;
        do {
            System.out.println("i is " + i);
            i++;
        } while (i < 5);
    }
}
