package LEARNING.JavaMethods;

public class javaMethodsBasic {
    static void sayName(String name, int age) {//You can define parameters inside as well
        //This is liek functions in python!
        //You define the function before you call main
        //You can run your functions after 
        System.out.println("Hello " + name + "!");
        System.out.println("You are " + age + " years old!");
    }

    static int add5(int x) { // void means that you won't return any values.
    // and data type means that you will return that datatype
        return x + 5;
    }
    public static void main(String[] args) {
        sayName("Joshua", 23);
        int num = add5(3);
        System.out.println(num);
    }   

    
}
