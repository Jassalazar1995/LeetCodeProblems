impl Solution {
    pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
        // Remove the extra zeros from the end of nums1
        nums1.truncate(m as usize);

        // Append nums2 to nums1
        nums1.append(nums2);

        // Sort the combined vector
        nums1.sort();
    }
}

fn main() {
    // Example usage
    let mut nums1 = vec![1, 2, 3, 0, 0, 0];
    let mut nums2 = vec![2, 5, 6];
    let m = 3;
    let n = 3;

    Solution::merge(&mut nums1, m, &mut nums2, n);
    println!("{:?}", nums1); // Should print [1, 2, 2, 3, 5, 6]

}