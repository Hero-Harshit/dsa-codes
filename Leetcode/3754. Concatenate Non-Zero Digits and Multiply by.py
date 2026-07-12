class Solution:
    def sumAndMultiply(self, n: int) -> int:
        # Peel off only the "living" digits — zeros don't get an invite to this party
        digits = [d for d in str(n) if d != '0']
        
        # If nobody showed up (all zeros, e.g. n = 0 or n = 000...), x = 0
        if not digits:
            return 0
        
        x = int(''.join(digits))
        total = sum(int(d) for d in digits)
        
        return x * total