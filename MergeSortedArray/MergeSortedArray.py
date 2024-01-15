class Solution:
    def merge(self, nums1, m, nums2, n):
        p1, p2, p = m - 1, n - 1, m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # Copy any remaining elements from nums2
        nums1[:p2 + 1] = nums2[:p2 + 1]

# Example usage
solution = Solution()
example1 = solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
example2 = solution.merge([1], 1, [], 0)
example3 = solution.merge([0], 0, [1], 1)

example1, example2, example3
