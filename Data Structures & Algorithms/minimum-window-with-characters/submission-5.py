from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s, t):
        if not s or not t or len(t) > len(s):
            return ''

        target = Counter(t)
        window = defaultdict(int)

        results = ''
        have = 0

        required = len(target)
        min_len = float('infinity')

        left = 0

        for right, char in enumerate(s):
            window[char] += 1

            if char in target and window[char] == target[char]:
                have += 1

            while have == required:
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    results = s[left:right + 1]

                left_char = s[left]
                window[left_char] -= 1

                if left_char in target and window[left_char] < target[left_char]:
                    have -= 1
                left += 1

        return results
