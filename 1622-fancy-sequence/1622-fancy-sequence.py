# borrowed solution from a friend to get a better understanding

class Fancy:
    """
    A data structure that maintains a sequence of numbers and supports:
    1. Appending new values
    2. Adding a constant to all elements
    3. Multiplying all elements by a constant
    4. Retrieving elements by index
    
    Key Insight: Instead of updating all elements on each addAll/multAll operation (which would be O(n)),
    we store elements in a "normalized" form and track transformations globally using lazy propagation.
    """
    
    def __init__(self):
        self.mod = 10**9 + 7  # All operations are modulo this prime number
        self.val = []  # Stores "normalized" values (inverse-transformed)
        
        # Global transformation trackers (represents: result = a * original + b)
        self.a = 1  # Global multiplier (starts at 1, meaning no multiplication yet)
        self.b = 0  # Global additive offset (starts at 0, meaning no addition yet)
    
    def append(self, val: int) -> None:
        """
        Appends a value to the sequence.
        
        Instead of storing val directly, we store it in "normalized" form by
        reversing the current global transformation (a, b).
        
        If the global state is: result = a * stored + b
        Then to store val, we need: stored = (val - b) / a
        
        We use modular multiplicative inverse: division by a becomes multiplication by a^(mod-2)
        (by Fermat's Little Theorem: a^(p-1) ≡ 1 (mod p), so a^(-1) ≡ a^(p-2) (mod p))
        """
        # Reverse the addition: val - b
        x = (val - self.b + self.mod) % self.mod
        
        # Reverse the multiplication: divide by a (multiply by modular inverse of a)
        # pow(self.a, self.mod - 2, self.mod) computes a^(-1) mod self.mod
        normalized = x * pow(self.a, self.mod - 2, self.mod) % self.mod
        self.val.append(normalized)
    
    def addAll(self, inc: int) -> None:
        """
        Adds 'inc' to all elements in the sequence.
        
        Since result = a * stored + b, adding inc to all results means:
        new_result = a * stored + (b + inc)
        
        So we just update the global offset b.
        """
        self.b = (self.b + inc) % self.mod
    
    def multAll(self, m: int) -> None:
        """
        Multiplies all elements in the sequence by 'm'.
        
        Since result = a * stored + b, multiplying all results by m means:
        new_result = m * (a * stored + b) = (m * a) * stored + (m * b)
        
        So we update both the global multiplier a and offset b.
        """
        self.a = (self.a * m) % self.mod
        self.b = (self.b * m) % self.mod
    
    def getIndex(self, idx: int) -> int:
        """
        Retrieves the element at index 'idx' after all transformations.
        
        We apply the current global transformation to the stored normalized value:
        result = a * stored_value + b
        """
        if idx >= len(self.val):
            return -1
        
        # Apply the global transformation: a * val[idx] + b
        return (self.a * self.val[idx] + self.b) % self.mod