'''

encode
i: list of strings
o: encoded string

decode
i: encoded string
o: list of strings

constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains any possible characters out of 256 valid ASCII characters.

time: O(n)
space: O()


ENCODE
init var to store encoded string

iterated though list of strings
append to var: len of string + string + delimiter
return encoded string

DECODE
init var to store delimiter


init var to store result

iterate through string
take the num from string, that will be how many positions to slice
push that string into results
increment pointer to next number and repeat
return results
'''


class Solution:

    def encode(self, strs: List[str]) -> str:

        delimiter = '#'
        res = []

        for word in strs:
            res.append(str(len(word)))
            res.append(delimiter)
            res.append(word)

        return ''.join(res)
    

    def decode(self, s: str) -> List[str]:
        delimiter = '#'
        res = []
        
        i = 0

        while i < len(s):
            j = i
            
            while s[j] != delimiter:
                j += 1

            length = int(s[i:j])

            left = j + 1
            right = left + length

            res.append(s[left:right])
            
            i = right 




        return res
            


