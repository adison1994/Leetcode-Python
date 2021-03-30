class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = ["0"] * len(s)
        i = 0
        for val in indices:
            result[val] = s[i]
            i = i + 1
        res_string = ""
        for i in range(len(result)):
            res_string = res_string + result[i]
        return res_string
        