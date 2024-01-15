func merge(nums1 []int, m int, nums2 []int, n int) []int {
    // Truncate nums1 to its actual size and append nums2
    nums1 = append(nums1[:m], nums2[:n]...)

    // Sort the combined slice
    sort.Ints(nums1)

    return nums1
}