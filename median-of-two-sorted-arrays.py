
# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)

        start = 0
        end = x

        while start <= end:
            partitionX = (start + end) // 2
            partitionY = ((x + y + 1) // 2) - partitionX

            # if partitionX is 0 it means nothing is there on left side. Use -INF for maxOfLeftX
            # if partitionX is length of input then there is nothing on right side. Use +INF for minOfRightX
            maxOfLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minOfRightX = float('inf') if partitionX == x else nums1[partitionX]

            maxOfLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minOfRightY = float('inf') if partitionY == y else nums2[partitionY]

            if maxOfLeftX <= minOfRightY and maxOfLeftY <= minOfRightX:
                # We have partitioned array at correct place
                # Now get max of left elements and min of right elements to get the median in case of even length
                # Or get max of left for odd length combined array size
                if (x + y) % 2 == 0:
                    return float(max(maxOfLeftX, maxOfLeftY) + min(minOfRightX, minOfRightY)) / 2
                else:
                    return max(maxOfLeftX, maxOfLeftY)

            # if maxOfLeftX > minOfRightY, move towards left side
            elif maxOfLeftX > minOfRightY:
                end = partitionX - 1
            # else, move towards right side
            else:
                start = partitionX + 1
