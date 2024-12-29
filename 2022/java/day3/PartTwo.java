import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Scanner;

public class PartTwo {
    public static void main(String[] args) {
        String path = "text.txt";
        int total = 0;
        try (Scanner scanner = new Scanner(Paths.get(path))) {
            ArrayList<Character> lettersInAll = new ArrayList<>();
            while (scanner.hasNextLine()) {
                String lineOne = scanner.nextLine();
                String lineTwo = scanner.nextLine();
                String lineThree = scanner.nextLine();

                for (int i = 0, size = lineOne.length(); i < size; i++) {
                    String letter = String.valueOf(lineOne.charAt(i));
                    if (lineTwo.contains(letter) && lineThree.contains(letter)) {
                        lettersInAll.add(lineOne.charAt(i));
                        break;
                    }
                }
            }
            for (char letter: lettersInAll) {
                int ascii = (int) letter;
                if (ascii >= 97 && ascii <= 122) {
                    total += ascii - 96;
                } else {
                    total += ascii - 38;
                }
            }
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
        System.out.println(total);
    }
}
