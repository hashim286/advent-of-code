import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Scanner;

public class PartOne {
    public static void main(String[] args) {
        int player_score = 0;

        String path = "text.txt";
        ArrayList<String> text = readFile(path);
        for (int i = 0, length = text.size(); i < length; i++) {
            String[] moves = text.get(i).split(" ");
            int opponentMove = translateMoveToNumber(moves[0]);
            int yourMove = translateMoveToNumber(moves[1]);
            player_score += determineWinner(opponentMove, yourMove) + yourMove;
        }
        System.out.println(player_score);
    }

    public static ArrayList<String> readFile(String path) {
        ArrayList<String> input = new ArrayList<>();
        
        try(Scanner scanner = new Scanner(Paths.get(path))) {
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                input.add(line);
            }
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
        return input;
    }

    public static int translateMoveToNumber(String input) {
        int pointsForRock = 1;
        int pointsForPaper = 2;
        int pointsForScissors = 3;

        if (input.equals("A") || input.equals("X")) {
            return pointsForRock;
        } else if (input.equals("B") || input.equals("Y")) {
            return pointsForPaper;
        } else {
            return pointsForScissors;
        }
    }

    public static int determineWinner(int moveOne, int moveTwo) {
        int pointsForWin = 6;
        int pointsForDraw = 3;
        int pointsForLoss = 0;

        if (moveTwo - moveOne == 1 || moveOne - moveTwo == 2) {
            return pointsForWin;
        } else if (moveTwo == moveOne) {
            return pointsForDraw;
        } else {
            return pointsForLoss;
        }
    }
}
