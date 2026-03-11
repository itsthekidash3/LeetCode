class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # Special case: complement of 0 is 1
        if n == 0:
            return 1
        
        # Step 1: Find how many bits we need to represent n
        # Example: n=5 (binary: 101) needs 3 bits
        num_bits = n.bit_length()
        
        # Step 2: Create a bitmask with all 1s of that length
        # (1 << num_bits) creates 2^num_bits, then subtract 1 to get all 1s
        # Example: (1 << 3) = 8 (binary: 1000), then 8-1 = 7 (binary: 111)
        bitmask = (1 << num_bits) - 1
        
        # Step 3: XOR n with the bitmask to flip all bits
        # Example: 5 (101) ^ 7 (111) = 2 (010)
        # XOR flips each bit: 1^1=0, 0^1=1, 1^1=0
        return n ^ bitmask