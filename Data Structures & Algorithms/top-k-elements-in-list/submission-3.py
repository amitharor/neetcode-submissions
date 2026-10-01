'''
i: int arr nums and int k
o: return k most freq elements in arr

constraints:
1 <= nums.length <= 10^4.
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums.

edge:

time: O()
space: O()





'''

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = Counter(nums)


        return [item[0] for item in count_nums.most_common(k)]
