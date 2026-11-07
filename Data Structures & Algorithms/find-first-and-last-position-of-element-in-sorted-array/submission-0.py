class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        bounds = []


        for value in (target, target + 1):
            left, right = 0, len(nums)

            while left < right:
                mid = (left + right) // 2

                if nums[mid] < value:
                    left = mid + 1
                else:
                    right = mid

            bounds.append(left)

        if bounds[0] == len(nums) or nums[bounds[0]] != target:
            return [-1, -1]

        return [bounds[0], bounds[1] - 1]