class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        count = start = 0

        while count < n:
            current = start
            prev = nums[start]

            while True:
                nextIndex = (current + k) % n
                nums[nextIndex], prev = prev, nums[nextIndex]
                current = nextIndex
                count += 1

                if start == current:
                    break

            start += 1