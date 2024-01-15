class Solution:
    def merge(self, nums1, m, nums2, n):
        # Copy nums2 to the end of nums1
        for i in range(n):
            nums1[m + i] = nums2[i]

        # Now sort the entire nums1 array
        nums1.sort()

        return nums1

# Test the method with the provided examples
sol = Solution()
example1 = sol.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
example2 = sol.merge([1], 1, [], 0)
example3 = sol.merge([0], 0, [1], 1)

example1, example2, example3