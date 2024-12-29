import java.io.IOException;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Scanner;
public class PartTwo {
    public static void main(String[] args) {
        String path = "text.txt";
        char[][] rowsWritten = {
                {'H', 'B', 'V', 'W', 'N', 'M', 'L', 'P'},
                {'M', 'Q', 'H'},
                {'N', 'D', 'B', 'G', 'F', 'Q', 'M', 'L'},
                {'Z', 'T', 'F', 'Q', 'M', 'W', 'G'},
                {'M', 'T', 'H', 'P'},
                {'C', 'B', 'M', 'J', 'D', 'H', 'G', 'T'},
                {'M', 'N', 'B', 'F', 'V', 'R'},
                {'P', 'L', 'H', 'M', 'R', 'G', 'S'},
                {'P', 'D', 'B', 'C', 'N'}
        };
        ArrayList<ArrayList<Character>> inputDataList = makeArrayList(rowsWritten);
        try(Scanner scanner = new Scanner(Paths.get(path))) {
            while (scanner.hasNextLine()) {
                int[] commandList = new int[3];
                String line = scanner.nextLine();
                String[] lineSplit = line.split(" ");
                boolean containsMove = false;
                for (String item: lineSplit) {
                    if (item.equals("move")) {
                        containsMove = true;
                        break;
                    }
                }

                if (containsMove) {
                    commandList[0] = Integer.parseInt(lineSplit[1]);
                    commandList[1] = Integer.parseInt(lineSplit[3]);
                    commandList[2] = Integer.parseInt(lineSplit[5]);
                } else {
                    continue;
                }

                int numItemsToMove = commandList[0];
                ArrayList<Character> row = inputDataList.get(commandList[1] - 1);
                ArrayList<Character> cratesBeingMoved = new ArrayList(row.subList(row.size() - numItemsToMove, row.size()));
                for (char crate: cratesBeingMoved) {
                    inputDataList.get(commandList[2] - 1).add(crate);
                }

                for (int i = 0; i < numItemsToMove; i++) {
                    ArrayList<Character> thisRow = inputDataList.get(commandList[1] - 1);
                    thisRow.remove(thisRow.size() - 1);
                }
            }
        } catch (IOException e) {
            System.out.println("Error: " + e.getMessage());
        }

        for (ArrayList<Character> item: inputDataList) {
            System.out.print(item.get(item.size() - 1));
        }
    }

    public static ArrayList<ArrayList<Character>> makeArrayList(char[][] data) {
        ArrayList<ArrayList<Character>> inputData = new ArrayList<>();
        for (char[] line: data) {
            ArrayList<Character> thisLine = new ArrayList<>();
            for (char character: line) {
                thisLine.add(character);
            }
            inputData.add(thisLine);
        }
        return inputData;
    }
}

