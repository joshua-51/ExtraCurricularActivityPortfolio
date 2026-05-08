package LEARNING.JavaMethods;

public class javaClasses {
    int x;

    public javaClasses(int x) {
        this.x = x;
    }
    public static void main(String[] args) {
        javaClasses myObj = new javaClasses(34);//First talk about the file, then talk about the class, and then ake an abject with the contents of the class
        System.out.println(myObj.x);
    }
}
