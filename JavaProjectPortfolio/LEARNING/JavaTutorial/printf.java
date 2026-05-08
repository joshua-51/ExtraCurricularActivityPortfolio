package LEARNING.JavaTutorial;

public class printf {

    String name = "Spongebob";
    char firstLetter = 'S';
    int age = 30;
    float height = 60.5f;
    boolean isEmployed = true;

    public static void main(String[] args) {
        printf spongebobInfo = new printf();
        System.out.printf("Hello %s\n", spongebobInfo.name);
        System.out.printf("You name starts with a %c\n", spongebobInfo.firstLetter);
        System.out.printf("You are %d years old\n", spongebobInfo.age);
        System.out.printf("You are %f inches tall\n", spongebobInfo.height);
        System.out.printf("Employed: %b\n", spongebobInfo.isEmployed);
        System.out.printf("%s is %d years old", spongebobInfo.name, spongebobInfo.age);
    }
}

class prices {
    double price1 = 9000.99;
    double price2 = 100.15;
    double price3 = -54.01;

    public static void main(String[] args) {
        prices prices = new prices();
        System.out.printf("%,.1f\n", prices.price1); //.1 is to chose how many decimal places you want after in you floating point. The comma adds a comma at every thousandths place
        System.out.printf("% +.2f\n", prices.price2); //this shows a positive alue fort he number The space adds a space after positive value to make them
        System.out.printf("%(.1f\n", prices.price3); // automatically adds parenthesis araound negative values.
    }
}

class ids {
    int id1 = 1;
    int id2 = 23;
    int id3 = 456;
    int id4 = 7890;
    static void zeroPadding() {
        ids ids = new ids();
        System.out.printf("%04d\n", ids.id1); //the zero tells java that you want a zero before ints with digits less than the number after zero
        System.out.printf("%04d\n", ids.id2);
        System.out.printf("%04d\n", ids.id3);
        System.out.printf("%04d\n", ids.id4);
    }

    static void leftPadding() {
        ids ids = new ids();
        System.out.printf("%-4d\n", ids.id1); // The negative tells is to left pad
        System.out.printf("%-4d\n", ids.id2);
        System.out.printf("%-4d\n", ids.id3);
        System.out.printf("%-4d\n", ids.id4);
    }
    public static void main(String[] args) {
        zeroPadding();
        leftPadding();
    }
}