// Has time complexity O(n^2)

public class TwoSums {

    // Separate method to find two numbers that add up to the target
    public static int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] {i, j};
                }
            }
        }
        return new int[] {}; // Return an empty array if no solution is found
    }

    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15}; // Example array
        int target = 9; // Example target
        int[] result = twoSum(nums, target); // Call the twoSum method

        if (result.length == 2) {
            System.out.println("Indices: " + result[0] + ", " + result[1]);
        } else {
            System.out.println("No solution found.");
        }
    }
}
