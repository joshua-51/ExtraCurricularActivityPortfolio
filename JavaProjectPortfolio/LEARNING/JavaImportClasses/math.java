package LEARNING.JavaImportClasses;

public class math {
    public static void main(String[] args) {
        double a = 64d;
        double b = -4d;
        double c = 3.33d;

        System.out.println(Math.max(a,b));
        System.out.println(Math.min(a,b));
        System.out.println(Math.sqrt(a));
        System.out.println(Math.abs(b));
        System.out.println(Math.pow(c,a));
        System.out.println(Math.round(c));
        System.out.println(Math.ceil(c));
        System.out.println(Math.floor(c));
        float random = (float)(Math.random());
        int randomNum = (int)(Math.random() * 101);
        System.out.println(random + "\n" + randomNum);
    }
}
