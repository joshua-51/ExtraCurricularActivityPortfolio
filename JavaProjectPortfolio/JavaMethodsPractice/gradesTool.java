package JavaMethodsPractice;
public class gradesTool {
    public static void main(String[] args) {
        int[] testScores = {85, 92, 45, 60, 95, 30, 88, 72};
        System.out.println(findHighest(testScores)+" was the highest score!");
        printFailing(testScores);
    }
    static int findHighest(int[] scores) {
        int max = scores[0];
        for (int score: scores) {
            if (score > max) {
                max = score;
            }
        }
        return max;
    }

    static void printFailing(int[] scores) {
        int i = 0;
        for (int score: scores) {
            if (score < 65 && i == 0){
                System.out.println("scores that failed - ");
                System.out.println(score);
                i++;
            } else if (score < 65) {
                System.out.println(score);
                i++;
            }
        }

        if (i==0) {
            System.out.println("Everyone Passed!");
        }
    }
}
