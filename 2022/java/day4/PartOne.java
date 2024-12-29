import java.io.IOException;
import java.nio.file.Paths;
import java.util.Scanner;

public class PartOne {
    public static void main(String[] args) {
        String path = "text.txt";
        int numberTotallyContained = 0;

        try (Scanner scanner = new Scanner(Paths.get(path))) {
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                String[] lineOneSplit = line.split(",");
                String[] boundsOne = lineOneSplit[0].split("-");
                String[] boundsTwo = lineOneSplit[1].split("-");
                numberTotallyContained += isTotallyContained(boundsOne, boundsTwo);
            }
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
        System.out.println(numberTotallyContained);
    }

    public static int isTotallyContained(String[] boundsOne, String[] boundsTwo) {
        int[] boundsOneInt = convertToInt(boundsOne);
        int[] boundsTwoInt = convertToInt(boundsTwo);
        int returnValue = 0;


        if (boundsOneInt[0] <= boundsTwoInt[0] && boundsOneInt[1] >= boundsTwoInt[1]) {
            returnValue = 1;
        } else if (boundsTwoInt[0] <= boundsOneInt[0] && boundsTwoInt[1] >= boundsOneInt[1]) {
            returnValue = 1;
        }

        return returnValue;
    }

    public static int[] convertToInt(String[] bounds) {
        int[] boundsInt = new int[2];
        for (int i = 0; i < bounds.length; i++) {
            boundsInt[i] = Integer.parseInt(bounds[i]);
        }
        return boundsInt;
    }
}
