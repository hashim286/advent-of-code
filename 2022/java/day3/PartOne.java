import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Scanner;

public class PartOne {
    public static void main(String[] args) {
        String path = "text.txt";
        int total = 0;
        try (Scanner scanner = new Scanner(Paths.get(path))) {
            while (scanner.hasNextLine()) {
                ArrayList<Character> lettersInCommon = new ArrayList<>();
                String line = scanner.nextLine();
                String firstHalf = line.substring(0, (int) line.length() / 2);
                String secondHalf = line.substring((int) line.length() / 2);
                for (int i = 0; i < firstHalf.length(); i++) {
                    String letter = String.valueOf(firstHalf.charAt(i));
                    if (secondHalf.contains(letter) && !lettersInCommon.contains(firstHalf.charAt(i))) {
                        lettersInCommon.add(firstHalf.charAt(i));
                    }
                }
                for (char letter: lettersInCommon) {
                    int ascii = (int) letter;
                    if (ascii >= 97 && ascii <= 122) {
                        total += ascii - 96;
                    } else {
                        total += ascii - 38;
                    }
                }

            }
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }

        System.out.println(total);
    }
}
