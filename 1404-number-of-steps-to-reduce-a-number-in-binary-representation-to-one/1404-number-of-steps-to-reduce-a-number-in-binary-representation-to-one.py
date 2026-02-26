# ⚠️ WARNING: s can be up to 500 chars, meaning num can be up to 2^500
# Python handles big integers natively so this works here,
# but in C++ or Java this would overflow — you'd need the string approach instead



class Solution:
    def numSteps(self, s: str) -> int:

        steps = 0
        num = int(s, 2)  # convert binary string to actual integer (e.g. "11101" → 29)

        while num != 1:  # keep going until we reduce down to 1
            steps += 1

            if num & 1 == 0:    # check last bit — if 0, number is even
                num //= 2       # divide by 2 (same as right shift)
            elif num & 1 == 1:  # if last bit is 1, number is odd
                num += 1        # adding 1 to an odd number makes it even, so next step will halve it

        return steps

        