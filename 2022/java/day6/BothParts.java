import java.io.IOException;
import java.nio.file.Paths;
import java.util.Scanner;

public class BothParts {
    public static void main(String[] args) {
        String path = "text.txt";
        // change read length to 4 or 14 to do either part
        int readLength = 14; //4
        String signal = readString(path);
        for (int i = 0, length = signal.length(); i < length; i++) {
            if (i == length - readLength) {
                break;
            }
            char[] letterList = new char[readLength];
            for (int j = 0; j < readLength; j++) {
                letterList[j] = signal.charAt(i + j);
            }

            if (checkIfAllUnique(letterList)) {
                System.out.println(i + readLength);
                break;
            }
        }
    }

    public static boolean checkIfAllUnique(char[] listOfLetters) {
        for (int i = 0, len = listOfLetters.length; i < len; i++) {
            for (int j = 0; j < len; j++) {
                if (i == j) {
                    break;
                }

                if (listOfLetters[i] == listOfLetters[j]) {
                    return false;
                }
            }
        }
        return true;
    }

    public static String readString(String path) {
        String signal = "";
        try(Scanner scanner = new Scanner(Paths.get(path))) {
            signal += scanner.nextLine();
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
        return signal;
    }
}
