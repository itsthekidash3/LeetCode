class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return 1 if n==0 else n^((1<<n.bit_length())-1) # n.bit_length() - Returns the number of bits needed to represent n in binary
                                                        # XOR : n ^ n' : 
                                                        # bitmask = (1<<n.bit_length()) - 1