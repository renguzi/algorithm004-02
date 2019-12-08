# class Solution:
#     def reverseBits(self, n):
#         res, mask = 0, 1
#
#         for i in range(32):
#             if n & mask:
#                 res |= 1 << (31 - i)
#             mask <<= 1
#         return res

# import re
# class Solution:
#     def myAtoi(self, s: str) -> int:
#         return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)


class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        before = ""
        after = ""

        mod = len(s) % (2 * k)
        handle_str = s
        if 2 * k > len(s):
            if mod <= k:
                after = s[-mod:][::-1]
            elif k < mod < 2 * k:
                after = s[-mod: -mod + k][::-1] + s[-mod + k:]
            return after
        elif 2 * k < len(s):
            if mod > 0:
                if mod < k:
                    after = s[-mod:][::-1]
                elif k < mod < 2 * k:
                    after = s[-mod: -mod + k][::-1] + s[-mod + k:]
                handle_str = s[:-mod]

        for i in range(int(len(handle_str) / (2 * k))):
            per_str = handle_str[i * 2 * k:2 * k * i + 2 * k]
            before += per_str[:k][::-1] + per_str[k:]
        return before + after


s = Solution()
print(s.reverseStr("abcd", 3))
