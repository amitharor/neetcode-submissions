class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr1, arr2 = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(arr2) < len(arr1):
            arr1, arr2 = arr2, arr1

        
        left, right = 0, len(arr1) - 1
        while True:
            mid = (left + right) // 2 #arr1
            mid2 = half - mid - 2 # arr2

            Aleft = arr1[mid] if mid >= 0 else float("-infinity")
            Aright = arr1[mid + 1] if (mid + 1) < len(arr1) else float("infinity")
            Bleft = arr2[mid2] if mid2 >= 0 else float("-infinity")
            Bright = arr2[mid2 + 1] if (mid2 + 1) < len(arr2) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bleft:
                right = mid - 1
            else:
                left = mid + 1

