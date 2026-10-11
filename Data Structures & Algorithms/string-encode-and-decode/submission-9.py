'''
input: array of strings
output: encoded string

input2: encoded string
output2: array of strings

constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains any possible characters out of 256 valid ASCII characters.


time: O(n)
space: O(n)

approach:

ENCODE:
init var to store delimiter
iterate through array
for each string, count the num of chars; append the char count + delmiter + word
return encoded string

DECODE:
init var to store delimiter
init var to store results

initialiate left/right pointers
iterate through string
find the num (keep incrementing until our delimiter, in case it's a multi digit number)
then the left pointer starts after the delimiter and the right pointer to the len of num (from prev step)
extract that word into results array
move the left pointer to right + 1
return results
'''





class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = '*'
        res = []

        for word in strs:
            res.append(
                str(len(word))
                + delimiter
                + word
            )

        return ''.join(res)

    def decode(self, s: str) -> List[str]:        
        delimiter = '*'
        left = right = 0
        res = []


        while left < len(s):
            while s[right] != delimiter:
                right += 1

            length = int(s[left:right])
            left = right + 1
            right = left + length
            res.append(s[left:right])

            left = right
            right = left
        
        return res






