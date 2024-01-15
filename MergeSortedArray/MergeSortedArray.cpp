#include <vector>
#include <algorithm> // For std::sort
using namespace std;

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        // Copy nums2 to the end of nums1
        for (int i = 0; i < n; ++i) {
            nums1[m + i] = nums2[i];
        }

        // Now sort the entire nums1 array
        sort(nums1.begin(), nums1.end());
    }
};