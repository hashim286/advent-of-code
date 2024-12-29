import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Day1 {
    public static void main(String[] args) {
        String path = "text.txt";
        // want to go through text.txt, find new line, add all  nums above, then add to list, return highest
        ArrayList<Integer> calorieTotals = makeList(path);
        int max = findMax(calorieTotals);
        ArrayList<Integer> topThree = topThree(calorieTotals);
        int topThreeSum = sumTopThree(topThree);
        System.out.println(max);
        System.out.println(topThreeSum);
    }

    public static ArrayList<Integer> makeList(String path) {
        int total = 0;
        ArrayList<Integer> calorieTotals = new ArrayList<>();
        try(Scanner scanner = new Scanner(Paths.get(path))) {
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                if (line.isEmpty()) {
                    calorieTotals.add(total);
                    total = 0;
                    continue;
                }
                int nums = Integer.parseInt(line);
                total += nums;
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        return calorieTotals;
    }

    public static int findMax(ArrayList<Integer> nums) {
        return Collections.max(nums);
    }

    public static ArrayList<Integer> topThree(ArrayList<Integer> nums) {
        ArrayList<Integer> topThree = new ArrayList<>();
        Collections.sort(nums);
        int lastElement = nums.size() - 1;
        topThree.add(nums.get(lastElement));
        topThree.add(nums.get(lastElement - 1));
        topThree.add(nums.get(lastElement - 2));
        return topThree;
    }

    public static int sumTopThree(ArrayList<Integer> topThree) {
        int total = 0;
        for (int num: topThree) {
            total += num;
        }
        return total;
    }
}
