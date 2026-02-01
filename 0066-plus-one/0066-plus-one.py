class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Traverse the digits from right to left (least significant → most significant)
        for i in range(len(digits) - 1, -1, -1):

            # If adding 1 does NOT cause a carry (digit becomes < 10)
            # we can increment and return immediately
            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits
            
            # Otherwise, adding 1 causes a carry:
            # set current digit to 0 and continue to the next digit on the left
            digits[i] = 0

            # If we are at the most significant digit and still have a carry,
            # it means the number was something like 999 → result is 1000
            if i == 0:
                return [1] + digits
